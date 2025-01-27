import logging
from pydantic import BaseModel
from fastapi import FastAPI, status
import uvicorn
from src.llm_service import LLMService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class UserInput(BaseModel):
    query : str

app = FastAPI()
ts = LLMService()

@app.get('/health', status_code=status.HTTP_200_OK)
async def perform_healthcheck():
    return {"health":"good!"}

@app.get("/getnode")
@app.post("/getnode")
async def get_node(input:UserInput):
    res=ts.text_to_node(input.query)
    return {"sequence": res}

if __name__ == "__main__":
    uvicorn.run('fastapi_main:app', host="0.0.0.0", port=8080)