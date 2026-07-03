from app.models import Patient
from app.validator import validate_patient


def test_valid_patient():

    patient = Patient(
        patient_id="12345",
        first_name="John",
        last_name="Doe",
        gender="M",
        dob="19800101",
        visit_type="OUTPATIENT"
    )

    errors = validate_patient(patient)

    assert len(errors) == 0


def test_missing_patient_id():

    patient = Patient(
        patient_id="",
        first_name="John",
        last_name="Doe",
        gender="M",
        dob="19800101",
        visit_type="OUTPATIENT"
    )

    errors = validate_patient(patient)

    assert len(errors) == 1


def test_invalid_gender():

    patient = Patient(
        patient_id="12345",
        first_name="John",
        last_name="Doe",
        gender="XYZ",
        dob="19800101",
        visit_type="OUTPATIENT"
    )

    errors = validate_patient(patient)

    assert len(errors) == 1
    assert "Invalid value" in errors[0].message