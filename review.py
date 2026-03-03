import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("app.js", "r") as file:
    code = file.read()

response = client.responses.create(
    model="gpt-4o-mini",
    input=f"""
You are a strict security reviewer.

If the code contains a hardcoded password like:
const password = "123456";

Respond ONLY with:
UNSAFE

If the password is read from environment variable like:
process.env.PASSWORD

Respond ONLY with:
SAFE

Here is the code:
{code}
"""
)

result = response.output_text.strip()

print("AI RESULT:", result)

if result == "UNSAFE":
    print("❌ Security issue found.")
    exit(1)
elif result == "SAFE":
    print("✅ Code is safe.")
    exit(0)
else:
    print("Unexpected response. Failing for safety.")
    exit(1)