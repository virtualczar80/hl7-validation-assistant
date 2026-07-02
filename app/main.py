from pathlib import Path
from app.parser import HL7Parser
from app.validator import validate_patient

BASE_DIR = Path(__file__).resolve().parent.parent

hl7_file = BASE_DIR / "sample_messages" / "adt_a01.hl7"

parser = HL7Parser(hl7_file)

patient = parser.get_patient()

print(patient)

errors = validate_patient(patient)

if errors:
    print("\nValidation Errors")

    for e in errors:
        print("-", e)

else:
    print("\nValidation Passed")