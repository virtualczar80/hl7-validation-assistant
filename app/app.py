from fastapi import FastAPI
from app.models import HL7Request
from app.service import process

app = FastAPI()


@app.get("/")
def home():
    return {
        "application": "HL7 Validation Assistant",
        "status": "Running",
        "docs": "/docs"
    }


@app.post("/validate")
def validate(request: HL7Request):
    return process(request.hl7)