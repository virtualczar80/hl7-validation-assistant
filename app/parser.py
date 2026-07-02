# from pathlib import Path
# from hl7apy.parser import parse_message
# from app.models import Patient


# # class HL7Parser:

# #     def __init__(self, hl7_text):
# #                 # Normalize HL7 segment separators
# #         hl7_text = "\r".join(
# #             line.strip()
# #             for line in hl7_text.splitlines()
# #             if line.strip()
# #         ) + "\r"

# #         self.message = parse_message(hl7_text, find_groups=False)

# #     def get_patient(self):

# #         pid = self.message.PID
# #         pv1 = self.message.PV1

# #         # Patient ID
# #         patient_id = pid.pid_3.to_er7().split("^")[0]

# #         # Patient Name
# #         name = pid.pid_5.to_er7().split("^")

# #         last_name = name[0] if len(name) > 0 else ""
# #         first_name = name[1] if len(name) > 1 else ""

# #         return Patient(
# #             patient_id=patient_id,
# #             first_name=first_name,
# #             last_name=last_name,
# #             gender=pid.pid_8.to_er7(),
# #             dob=pid.pid_7.to_er7(),
# #             visit_type=pv1.pv1_2.to_er7()
# #         )
# # from hl7apy.parser import parse_message

# class HL7Parser:

#     def __init__(self, hl7_text):

#         print("Raw input:")
#         print(repr(hl7_text))

#         # Normalize all line endings
#         segments = [
#             line.strip()
#             for line in hl7_text.splitlines()
#             if line.strip()
#         ]

#         normalized = "\r".join(segments) + "\r"

#         print("Normalized:")
#         print(repr(normalized))

#         self.message = parse_message(normalized, find_groups=False)
from hl7apy.parser import parse_message
from app.models import Patient


class HL7Parser:

    def __init__(self, hl7_text: str):

        # Normalize every type of newline
        segments = [
            line.strip()
            for line in hl7_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
            if line.strip()
        ]

        normalized = "\r".join(segments) + "\r"

        self.message = parse_message(normalized, find_groups=False)

    def get_patient(self):

        pid = self.message.PID
        pv1 = self.message.PV1

        patient_id = pid.pid_3.to_er7().split("^")[0]

        name = pid.pid_5.to_er7().split("^")

        return Patient(
            patient_id=patient_id,
            last_name=name[0],
            first_name=name[1],
            gender=pid.pid_8.to_er7(),
            dob=pid.pid_7.to_er7(),
            visit_type=pv1.pv1_2.to_er7(),
        )