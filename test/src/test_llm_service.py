import unittest
from unittest.mock import Mock, patch
from src.llm_service import LLMService

class TestLLMService(unittest.TestCase):
    def test_text_to_node_caching(self):
        # Create LLMService instance
        service = LLMService()
        
        # Mock the model.invoke to track calls
        with patch.object(service.model, 'invoke', return_value='test_output') as mock_invoke:
            
            # Call with same input twice
            result1 = service.text_to_node("test input")
            result2 = service.text_to_node("test input") 
            
            # Verify results are same
            self.assertEqual(result1, result2)
            
            # Verify invoke was called only once
            mock_invoke.assert_called_once()

if __name__ == '__main__':
    unittest.main()