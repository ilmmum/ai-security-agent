import os

with open("app.js", "r") as file:
    code = file.read()

print("Simulated AI checking code...")

if 'process.env.PASSWORD' in code:
    print("AI RESULT: SAFE")
    exit(0)
else:
    print("AI RESULT: UNSAFE")
    exit(1)