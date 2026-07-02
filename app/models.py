from dataclasses import dataclass
from pydantic import BaseModel
class HL7Request(BaseModel):
   hl7:str

@dataclass
class Patient:

    patient_id: str
    first_name: str
    last_name: str
    gender: str
    dob: str
    visit_type: str
class ValidationError(BaseModel):
    field: str
    name: str
    severity: str
    message: str