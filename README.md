# Text to Sequence Application

This application comprises two main components:  
- **FastAPI server** running on port **8080**  
- **Streamlit UI** running on port **8501**  

## Features
- The **FastAPI documentation** can be accessed at: [http://localhost:8080/docs](http://localhost:8080/docs).
- The code is designed to be modular, allowing you to:
  - Replace `openai_model.py` with any compatible model.
  - Customize the prompt to suit specific model requirements.  
    This enables integration with various models like Hugging Face or Gemini.

## Setup and Execution Instructions
Follow these steps to create and run the application:  
1. Generate an OpenAI API key from the OpenAI website.  
   - Save the key as an environment variable named `OPENAI_API_KEY`.  
2. Navigate to the directory containing the application code.  
3. Build the Docker image:  
   ```bash
   docker build -t texttoseq_app .
4. Run the container using the following command:
    ```
    docker run -p 8080:8080 -p 8501:8501 -e OPENAI_API_KEY=$OPENAI_API_KEY texttoseq_app

## Evaluation
- For assessing the output quality, refer to the notebook: evaluation.ipynb.
    - The evaluation method compares model outputs against ground truth data and computes an accuracy score.