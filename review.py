import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("app.js", "r") as file:
    code = file.read()

response = client.responses.create(
    model="gpt-4o-mini",
    input=f"""
You are a security reviewer.
Reply ONLY with SAFE or UNSAFE.

Is this code secure?

{code}
"""
)

result = response.output_text.strip()

print("AI RESULT:", result)

if "UNSAFE" in result:
    print("❌ Security issue found.")
    exit(1)
else:
    print("✅ Code is safe.")
    exit(0)