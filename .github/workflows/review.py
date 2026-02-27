import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("app.js", "r") as file:
    code = file.read()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a security code reviewer."},
        {"role": "user", "content": f"Check this code for vulnerabilities:\n{code}"}
    ]
)

result = response.choices[0].message.content

print(result)

if "hardcoded" in result.lower():
    print("❌ Security issue found. Failing pipeline.")
    exit(1)
else:
    print("✅ No critical issue found.")
    exit(0)