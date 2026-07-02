from fastapi import FastAPI, Body
from app.models import HL7Request
from app.service import process


app = FastAPI()


@app.post("/validate")
def validate(request: HL7Request):
    return process(request.hl7)


