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
        kwds.setdefault('model', 'gpt-4o')
        return super().invoke(*args, **kwds)

class GPT_4o_mini_model(GPT):
    @timer("gpt 4o mini took: ")
    def invoke(self,*args, **kwds):
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