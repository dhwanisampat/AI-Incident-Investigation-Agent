# AI Incident Investigation Agent

## Overview

The AI Incident Investigation Agent is a FastAPI-based web application that helps analyze application and infrastructure log files using AI.

The application allows users to upload log files, extracts important events such as errors and warnings, summarizes the logs, and uses a Large Language Model (LLM) to identify the probable root cause of an incident along with severity, investigation commands, and recommended resolutions.

---

## Features

- Upload `.log` and `.txt` files
- Automatic log parsing and summarization
- Detection of:
  - Errors
  - Warnings
  - Critical events
  - Tracebacks
- AI-powered incident investigation
- Incident classification
- Severity prediction
- Root cause analysis
- Linux investigation commands
- Python debugging checks
- Recommended resolutions
- Copy-to-clipboard support for commands
- Clean web interface built using FastAPI and Jinja2 Templates

---

## System Architecture

```text
               User
                 │
                 ▼
      Upload Log File (.log/.txt)
                 │
                 ▼
         FastAPI Web Application
                 │
        ┌────────┴────────┐
        ▼                 ▼
  Log Parser         Incident Agent
        │                 │
        │          OpenRouter API
        │                 │
        └────────┬────────┘
                 ▼
        AI Investigation Result
                 │
                 ▼
        Interactive Dashboard
```

---

## Technology Stack

- Python
- FastAPI
- Jinja2 Templates
- HTML
- CSS
- JavaScript
- OpenRouter API
- DeepSeek Chat Model
- Git
- GitHub

---

## Project Structure

```text
AI-Incident-Investigation-Agent/
│
├── app.py
├── agent.py
├── log_parser.py
├── requirements.txt
├── sample_logs/
├── uploads/
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## How It Works

1. User uploads a log file.
2. The Log Parser extracts important information such as errors, warnings, tracebacks, and critical events.
3. A structured log summary is prepared.
4. The Incident Agent sends the summary to the AI model.
5. The AI identifies:
   - Incident Type
   - Severity
   - Confidence
   - Root Cause
   - Linux Commands
   - Python Checks
   - Recommended Resolution
6. The results are displayed on the dashboard.

---

## Sample Output
<img width="1158" height="621" alt="image" src="https://github.com/user-attachments/assets/6efc927d-c4ef-4696-8d94-3683f0c1a0e5" />

<img width="1084" height="704" alt="image" src="https://github.com/user-attachments/assets/84edcd0a-765d-41d6-8636-0a931cb1498c" />

<img width="1111" height="510" alt="image" src="https://github.com/user-attachments/assets/d1b1a635-613a-4356-8802-477eda3c2bbd" />

<img width="1118" height="632" alt="image" src="https://github.com/user-attachments/assets/c4d45c5a-5916-4dbb-9306-2656d8794935" />

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dhwanisampat/AI-Incident-Investigation-Agent.git
```

Navigate to the project:

```bash
cd AI-Incident-Investigation-Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:8000
```

---

## Author

**Dhwani Sampat**
LinkedIn: linkedin.com/in/dhwanisampat/
Github: https://github.com/dhwanisampat
