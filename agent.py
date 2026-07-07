import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM_PROMPT = """
You are a Senior DevOps Site Reliability Engineer.

Analyze the supplied log summary.

Return ONLY valid JSON.
Do NOT use markdown.
Do NOT use ```json.
Do NOT add explanations before or after the JSON.

Return exactly this schema:

{
  "incident_type": "",
  "severity": "",
  "confidence": "",
  "root_cause": "",
  "detected_errors": [],
  "detected_warnings": [],
  "linux_commands": [],
  "python_checks": [],
  "resolution": []
}

Rules:

incident_type:
Database
Network
Linux OS
Python
Docker
Kubernetes
Memory
Disk
Application

severity:
Low
Medium
High
Critical

confidence:
Percentage like "92%"

linux_commands:
Always return at least 5 Linux commands useful for investigating the detected incident.
Never return an empty array.

python_checks:
Always return at least 3 Python commands or scripts that help investigate the detected incident.
Never return an empty array.

detected_errors:
Return an array containing the most important ERROR messages found in the supplied log summary.

detected_warnings:
Return an array containing the most important WARNING messages found in the supplied log summary.

resolution:
Array of recommended fixes.

If there are no errors or warnings, return empty arrays.

Always include every field in the schema, even if its value is an empty array or an empty string.

Never omit any field.

Return JSON only.
"""


class IncidentAgent:

    def analyze(self, summary):

        user_message = f"""
Analyze this log summary.

Total Lines:
{summary.get('total_lines')}

Total Errors:
{summary.get('total_errors')}

Total Warnings:
{summary.get('total_warnings')}

First Error:
{summary.get('first_error')}

Last Error:
{summary.get('last_error')}

Detected Errors:
{summary.get('detected_errors')}

Detected Warnings:
{summary.get('detected_warnings')}

Tracebacks:
{summary.get('tracebacks')}

Critical Events:
{summary.get('critical_events')}

Use all of the above information to determine the actual root cause.

Populate every JSON field accurately.

If errors or warnings are available, return them in detected_errors and detected_warnings.

Return valid JSON only.
"""

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Incident Investigation Agent"
        }

        payload = {
            "model": "deepseek/deepseek-chat-v3-0324",
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.2
        }

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload
        )

        print("=" * 80)
        print("STATUS:", response.status_code)
        print(response.text)
        print("=" * 80)

        response.raise_for_status()

        data = response.json()

        raw_content = data["choices"][0]["message"]["content"].strip()

        # Remove markdown if the AI accidentally returns it
        if raw_content.startswith("```"):
            raw_content = raw_content.replace("```json", "")
            raw_content = raw_content.replace("```", "")
            raw_content = raw_content.strip()

        try:
            parsed = json.loads(raw_content)

        except Exception as e:
            print("JSON PARSE ERROR:", e)
            print(raw_content)

            parsed = {
                "incident_type": "Unknown",
                "severity": "Unknown",
                "confidence": "0%",
                "root_cause": "Failed to parse AI response as JSON.",
                "detected_errors": [],
                "detected_warnings": [],
                "linux_commands": [],
                "python_checks": [],
                "resolution": []
            }

        return parsed