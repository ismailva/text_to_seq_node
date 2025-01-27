import unittest
from src.openai_model import GPT_4o_model
from src.llm_model import LLMModel

class TestLLMModel(unittest.TestCase):
    
    def test_get_model_with_gpt4o(self):
        model_name = "gpt4o"
        model_instance = LLMModel.get_model(model_name)
        self.assertIsInstance(model_instance, GPT_4o_model)

if __name__ == "__main__":
    unittest.main()