from typing import List, Dict
from openai import OpenAI
from abc import ABC, abstractmethod
from src.utils import timer
from src.constants import OPENAI_KEY

class GPT(ABC):
    def __init__(self):
        self.model = OpenAI(api_key=OPENAI_KEY, timeout=60, max_retries=0)

    @abstractmethod
    def invoke(self,*args, **kwds):
        """
        Invokes the OpenAI API with the provided arguments and returns the response.

        This method handles the core API interaction logic for all GPT model variants.
        It processes both structured (with response_format) and unstructured responses.

        Args:
            *args: Variable length argument list passed to the OpenAI API call
            **kwds: Arbitrary keyword arguments. Common parameters include:
                - messages: List of message dictionaries with role and content
                - response_format: Optional format specification for structured responses
                - temperature: Controls randomness in the output (defaults to 0)
                - model: The specific GPT model to use (set by child classes)

        Returns:
            str: For unstructured responses, returns the raw completion text
                 For structured responses, returns a string representation of node sequence

        Raises:
            Exception: Prints any errors encountered during API interaction
        """
        kwds.setdefault('temperature', 0)
        nodes_seq = []
        final_response = ""
        try:
            if "response_format" in kwds:
                openai_response=self.model.beta.chat.completions.parse(*args, **kwds)
                response = openai_response.choices[0].message.parsed
                for relation in response.all_nodes:
                    nodes_seq.append(relation.value)
                final_response=str(nodes_seq)
            else:
                response = self.model.chat.completions.create(*args, **kwds)
                final_response = response.choices[0].message.content
        except Exception as e:
            print(e)
        return final_response

class GPT_4o_model(GPT):
    @timer("gpt 4o took: ")
    def invoke(self,*args, **kwds):
        """
        Invokes the GPT-4o model with the provided arguments and returns the response.
        """
        kwds.setdefault('model', 'gpt-4o')
        return super().invoke(*args, **kwds)

class GPT_4o_mini_model(GPT):
    @timer("gpt 4o mini took: ")
    def invoke(self,*args, **kwds):
        """
        Invokes the GPT-4o mini model with the provided arguments and returns the response.
        """
        kwds.setdefault('model', 'gpt-4o-mini')
        return super().invoke(*args, **kwds)

if __name__ == "__main__":
    kwargs = {
        "messages" : [
        {"role":"system", "content": "you are a bot"},
        {"role" : "user" , "content" : "What is the meaning of life"}],
    }
    
    gpt = GPT_4o_mini_model()
    print(gpt.invoke(**kwargs))