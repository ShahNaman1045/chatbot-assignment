from fastapi import FastAPI
from pydantic import BaseModel
from logic import classify_message
from llm import generate_response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    email: str


@app.post("/chat")
def chat(req: ChatRequest):

    # authentication guardrail
    if not req.email.endswith("@petasight.com"):
        return {"error": "Access restricted"}
    
    msg_type, color = classify_message(req.message)
    response = generate_response(req.message)

    return {
        "type": msg_type,
        "color": color,
        "response": response
    }
