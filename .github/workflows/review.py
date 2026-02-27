import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("app.js", "r") as file:
    code = file.read()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a security reviewer. Respond ONLY with PASS or FAIL. If secure, respond PASS. If insecure, respond FAIL."
        },
        {
            "role": "user",
            "content": f"Check this code:\n{code}"
        }
    ]
)

result = response.choices[0].message.content.strip()

print("AI RESPONSE:", result)

if result == "PASS":
    print("✅ Pipeline Passing")
    exit(0)
else:
    print("❌ Pipeline Failing")
    exit(1)