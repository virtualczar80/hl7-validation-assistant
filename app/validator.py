from app.models import ValidationError
from app.rules import PATIENT_RULES


def validate_patient(patient):

    errors = []

    for attribute, rule in PATIENT_RULES.items():

        value = getattr(patient, attribute)

        # Required field validation
        if rule.required and not value:
            errors.append(
                ValidationError(
                    field=rule.field,
                    name=rule.name,
                    severity="Error",
                    message=f"{rule.name} is required."
                )
            )
            continue

        # Allowed values validation
        if (
            rule.allowed_values
            and value
            and value not in rule.allowed_values
        ):
            errors.append(
                ValidationError(
                    field=rule.field,
                    name=rule.name,
                    severity="Error",
                    message=f"Invalid value '{value}'. "
                            f"Expected one of {sorted(rule.allowed_values)}."
                )
            )

    return errors