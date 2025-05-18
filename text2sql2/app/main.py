from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from app.core import say_hello
from text2sql2.agent.run import dummy_func

# python -m uvicorn text2sql2.app.main:app --reload
app = FastAPI()

# Allow CORS so Streamlit (running elsewhere) can call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific domain
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/hello")
def get_hello_message(data: TextInput):
    result = dummy_func(data.text)
    return {"message": result}