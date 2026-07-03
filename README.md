# 🏥 Madhusudan's HL7 Validation Assistant

An AI-powered HL7 v2.x message validation application built with **FastAPI**, **Streamlit**, and **Ollama**.

The application validates HL7 patient messages against configurable business rules and provides AI-generated explanations for validation errors using a locally running Large Language Model (LLM).

---

## 🚀 Features

* Parse HL7 v2.x messages
* Extract patient information from PID segments
* Validate patient demographics
* Configurable validation rules
* AI-powered error explanations using Ollama
* FastAPI REST API
* Streamlit web interface
* Upload HL7 (.hl7/.txt) files
* Paste single or multiple HL7 messages
* Batch validation support
* JSON API responses

---

## 🛠️ Technology Stack

| Component       | Technology         |
| --------------- | ------------------ |
| Backend         | FastAPI            |
| Frontend        | Streamlit          |
| Language        | Python             |
| HL7 Parsing     | hl7apy             |
| AI              | Ollama (Local LLM) |
| HTTP Client     | Requests           |
| Version Control | Git                |
| Repository      | GitHub             |

---

## 📁 Project Structure

```text
hl7-validation-assistant/
│
├── app/
│   ├── app.py
│   ├── ai.py
│   ├── parser.py
│   ├── validator.py
│   ├── service.py
│   ├── batch_processor.py
│   ├── prompt.py
│   └── ...
│
├── ui/
│   ├── app.py
│   └── config.py
│
├── sample_messages/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/virtualczar80/hl7-validation-assistant.git
cd hl7-validation-assistant
```

### Create a virtual environment

Windows

```bash
python -m venv venv
```

Activate the environment

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the required model (example):

```bash
ollama pull llama3.2
ollama run llama3.2:3b
```

<!-- Start Ollama:

```bash
ollama serve
```

--- -->

## ▶️ Running the Application

### Start the FastAPI server

```bash
uvicorn app.app:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

### Start the Streamlit UI

Open another terminal.

```bash
streamlit run ui/app.py
```

Open:

```
http://localhost:8501
```

---

## 📋 Validation Rules

Current validations include:

* Patient ID is mandatory
* First Name is mandatory
* Last Name is mandatory
* Gender must contain a valid HL7 value
* Date of Birth validation
* Configurable business rules

---

## 🧠 AI-Powered Validation

For every validation error, the application generates an easy-to-understand explanation using a locally running LLM through Ollama.

Example:

```
Validation Error:
Gender contains an invalid value.

AI Explanation:
HL7 Administrative Sex must contain one of the valid values
(M, F, U, O, A, N depending on HL7 version).
```

---

## 📷 Screenshots

Coming Soon

* Dashboard
* Validation Results
* Batch Processing
* AI Explanations

---

## 🔮 Future Enhancements

* Dashboard metrics
* Validation history
* SQLite database
* CSV/PDF report export
* Docker support
* User authentication
* Role-based access
* Audit logging
* HL7 ORM/ORU/SIU support
* FHIR validation
* Cloud deployment
* Unit tests with pytest

---

## 👨‍💻 Author

**Madhusudan Vedayas**

GitHub: https://github.com/virtualczar80

---

## 📄 License

This project is licensed under the MIT License.
