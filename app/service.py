from fastapi import HTTPException
from app.parser import HL7Parser
from app.validator import validate_patient
from app.ai import explain_error
from app.batch_processor import split_messages

def process(hl7_text: str):

    messages = split_messages(hl7_text)

    if len(messages) == 1:
        return process_message(messages[0])

    return process_messages(hl7_text)

def process_message(hl7_text: str):

    try:
        parser = HL7Parser(hl7_text)

        patient = parser.get_patient()

        errors = validate_patient(patient)
        enhanced_errors = []
        for error in errors:
            item = error.model_dump()

            item["ai_explanation"] = explain_error(error)

            enhanced_errors.append(item)

        return {
            "status": "Valid" if not errors else "Invalid",
            "patient": patient.__dict__,
            "errors":enhanced_errors
        }

    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex)
        )
def process_messages(file_text: str):
    
   # Process a file containing one or more HL7 messages.
    

    messages = split_messages(file_text)

    results = []

    for index, message in enumerate(messages, start=1):

        try:
            result = process_message(message)

            results.append({
                "message_number": index,
                "result": result
            })

        except HTTPException as ex:

            results.append({
                "message_number": index,
                "status": "Invalid",
                "error": ex.detail
            })

    return {
        "total_messages": len(messages),
        "results": results
    }