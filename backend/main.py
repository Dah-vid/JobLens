from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
import anthropic
import json

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
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Extract the following from this job description and return as JSON only, no other text:
                {{
                    "job_title": "string",
                    "required_skills": "string",
                    "seniority_level": "string",
                    "salary": "string or null if not mentioned"
                }}
                
                Job description: {job.description}"""
            }
        ]
    )
    raw = message.content[0].text
    cleaned = raw.strip().removeprefix("```json").removesuffix("```").strip()
    extracted = json.loads(cleaned)
    return {"result": extracted}