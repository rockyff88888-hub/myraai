from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate(data: Prompt):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional web developer."
            },
            {
                "role": "user",
                "content": f"Create full responsive website code for: {data.prompt}"
            }
        ]
    )

    return {
        "code": response.choices[0].message.content
    }
