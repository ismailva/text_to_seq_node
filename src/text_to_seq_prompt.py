from pathlib import Path
from typing import List
from string import Template
from src.utils import SingletonClass
from src import constants
from src.openai_model import GPT
import json
from enum import Enum
from pydantic import BaseModel

DATA_FOLDER = Path(__file__).parent.parent.joinpath("data")

class TextToSeqPrompt(metaclass=SingletonClass):
    def __init__(self):
        with open(DATA_FOLDER.joinpath("prompt_node_seq.txt"), "r") as file:
            temp = Template(file.read())
        with open(DATA_FOLDER.joinpath("list_of_all_nodes.json"), "r") as file:
            json_data = json.load(file)
        combined_items = {}
        for category_values in json_data.values():
            combined_items.update(category_values)
        json_text = json.dumps(json_data, indent=4)

        self.EnumClass = Enum('Nodes', {key: key for key in combined_items.keys()})
        self.prompt = Template(temp.safe_substitute(JSON_SCHEMA=json_text))
    
    def convert_to_gpt_format(self, user_input):
        text_prompt = self.prompt.substitute(query=user_input)
        system_prompt, user_prompt = text_prompt.split(constants.SYSTEM_SEPARATOR)
        class SequenceOfNodes(BaseModel):
            all_nodes: List[self.EnumClass]
        kwargs = {
            "messages" : [
            {"role":"system", "content": system_prompt},
            {"role" : "user" , "content" : user_prompt}],
            "response_format": SequenceOfNodes
        }
        return kwargs

    def convert_to_model_required_format(self, llm_model, user_input):
        if isinstance(llm_model, GPT):
            final_prompt = self.convert_to_gpt_format(user_input)
        return final_prompt
