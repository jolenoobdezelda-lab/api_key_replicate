from fastapi import FastAPI
from pydantic import BaseModel
import replicate

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: Prompt):
    output = replicate.run(
        "stability-ai/sdxl:latest",
        input={"prompt": prompt.text}
    )
    return {"image": output[0]}