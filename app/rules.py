from dataclasses import dataclass
from app.constants import VALID_GENDERS


@dataclass
class ValidationRule:
    field: str
    name: str
    required: bool = True
    allowed_values: set | None = None


PATIENT_RULES = {
    "patient_id": ValidationRule(
        field="PID-3",
        name="Patient Identifier"
    ),

    "last_name": ValidationRule(
        field="PID-5.1",
        name="Last Name"
    ),

    "first_name": ValidationRule(
        field="PID-5.2",
        name="First Name"
    ),

    "gender": ValidationRule(
        field="PID-8",
        name="Administrative Gender",
        allowed_values=VALID_GENDERS
    )
}