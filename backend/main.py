from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
import anthropic
load_dotenv()
app = FastAPI()
client = anthropic.Anthropic()

class JobInput(BaseModel):
    description: str

@app.get("/")
def health_check():
    return {"status": "we live"}

@app.post("/jobs")
def create_job(job: JobInput):
    return {"received": job}