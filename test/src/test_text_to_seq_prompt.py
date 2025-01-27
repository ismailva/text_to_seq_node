import unittest
from src.text_to_seq_prompt import TextToSeqPrompt
from src.openai_model import GPT_4o_mini_model
from unittest.mock import MagicMock

class MockGPT(GPT_4o_mini_model):
    def invoke(self, **kwargs):
        return ["Node1", "Node2"]

class TestTextToSeqPrompt(unittest.TestCase):
    def setUp(self):
        self.text_to_seq = TextToSeqPrompt()

    def test_convert_to_gpt_format(self):
        test_input = "test query"
        test_output = "test query\n"
        
        result = self.text_to_seq.convert_to_gpt_format(test_input)
        
        # we are checking below if input is converted to gpt format
        self.assertIsInstance(result, dict)
        self.assertIn("messages", result)
        self.assertIn("response_format", result)
        self.assertEqual(len(result["messages"]), 2)
        self.assertEqual(result["messages"][1]["content"], test_output)

    def test_convert_to_model_required_format_gpt(self):
        test_input = "test query"
        mock_gpt_model = GPT_4o_mini_model()
        self.text_to_seq.convert_to_gpt_format = MagicMock()
        self.text_to_seq.convert_to_model_required_format(mock_gpt_model, test_input)
        
        # we are checking below if model is gpt then convert_to_gpt_format should be called
        self.text_to_seq.convert_to_gpt_format.assert_called_once_with(test_input)
        

if __name__ == '__main__':
    unittest.main()