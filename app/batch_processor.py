from typing import List


def split_messages(file_text: str) -> List[str]:
    """
    Splits a file containing one or more HL7 messages into
    individual HL7 message strings.

    Each HL7 message is expected to start with an MSH segment.

    Args:
        file_text: Entire contents of the HL7 file.

    Returns:
        List of HL7 message strings.
    """

    messages = []
    current_message = []

    for line in file_text.splitlines():

        line = line.strip()

        # Ignore blank lines
        if not line:
            continue

        # New message starts
        if line.startswith("MSH|"):

            # Save previous message
            if current_message:
                messages.append("\r".join(current_message))

            # Start new message
            current_message = [line]

        else:
            current_message.append(line)

    # Add the last message
    if current_message:
        messages.append("\r".join(current_message))

    return messages