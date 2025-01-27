from typing import Any

from src.utils import SingletonClass
from src.openai_model import GPT_4o_model, GPT_4o_mini_model

class LLMModel(metaclass=SingletonClass):
    def get_model(model_name:str="gpt4o") -> Any:
        if model_name == "gpt4o":
            model_instance = GPT_4o_model()
        elif model_name == "gpt4o-mini":
            model_instance = GPT_4o_mini_model()
        return model_instance
