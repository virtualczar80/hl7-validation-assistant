import streamlit as st
import requests
from config import API_BASE_URL

st.set_page_config(
    page_title="Madhusudan's HL7 Validation Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Madhusudan's HL7 Validation Assistant")

st.write("Upload an HL7 file or paste an HL7 message below.")

# ----------------------------------------
# Upload HL7 File
# ----------------------------------------

hl7_message = ""

uploaded_file = st.file_uploader(
    "Upload HL7 File",
    type=["hl7", "txt"]
)

if uploaded_file:
    hl7_message = uploaded_file.read().decode("utf-8")
    #st.write("File uploaded successfully!")
    #st.code(hl7_message, language="text")

# ----------------------------------------
# HL7 Text Area
# ----------------------------------------

hl7_message = st.text_area(
    "HL7 Message",
    value=hl7_message,
    height=300
)

# ----------------------------------------
# Validate Button
# ----------------------------------------

if st.button("Validate"):

    if not hl7_message.strip():
        st.warning("Please upload or paste an HL7 message.")
        st.stop()

    with st.spinner("Validating HL7 message..."):
         #st.write("Calling API...")

       # endpoint = "/validate/batch" if uploaded_file else "/validate/json"

         response = requests.post(
        f"{API_BASE_URL}/validate",
        json={
        "hl7": hl7_message},
        timeout=120
    
    )
   # st.write("API response received")
    if response.status_code == 200:
            result = response.json()
            st.json(result)
            st.stop()

            st.success(f"Status: {result['status']}")

            # -------------------------
            # Patient Information
            # -------------------------

            patient = result.get("patient", {})

            st.subheader("👤 Patient Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Patient ID:** {patient.get('patient_id', '')}")
                st.write(f"**First Name:** {patient.get('first_name', '')}")

            with col2:
                st.write(f"**Last Name:** {patient.get('last_name', '')}")
                st.write(f"**Gender:** {patient.get('gender', '')}")

            # -------------------------
            # Validation Errors
            # -------------------------

            st.subheader("📋 Validation Results")

            errors = result.get("errors", [])

            if errors:
                for error in errors:
                    with st.expander(f"❌ {error.get('field', '')}"):
                        st.write(f"**Field:** {error.get('field', '')}")
                        st.write(f"**Message:** {error.get('message', '')}")
                        if "ai_explanation" in error:
                            st.info(error["ai_explanation"])
            else:
                st.success("🎉 No validation errors found!")
    else:
            st.error(f"Error {response.status_code}")
            st.code(response.text)

