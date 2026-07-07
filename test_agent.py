from agent import IncidentAgent

sample_summary = {
    "total_lines": 31,
    "total_errors": 5,
    "total_warnings": 2,
    "first_error": "Database connection timeout",
    "last_error": "Traceback"
}

agent = IncidentAgent()

response = agent.analyze(sample_summary)

print("\n===== AI RESPONSE =====\n")
print(response)