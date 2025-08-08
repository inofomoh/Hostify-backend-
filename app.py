from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Hostify Backend is Live!"}

@app.post("/generate")
def generate_code(input: PromptInput):
    prompt = input.prompt
    # Dummy logic: You can replace this with AI or actual generation
    generated_code = f"# Code generated for: {prompt}\nprint('Hello from Hostify!')"
    return {
        "input": prompt,
        "output": generated_code
    }
