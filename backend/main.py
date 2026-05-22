from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv
from database import get_connection


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
                    "extracted_skills": "string",
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jobs (job_title, extracted_skills, seniority_level, salary) VALUES (%s, %s, %s, %s)", (extracted["job_title"], extracted["extracted_skills"], extracted["seniority_level"], extracted["salary"]) )
    conn.commit()
    cursor.close()
    conn.close()
    return {"result": extracted}

#test
#test 2
#test 3