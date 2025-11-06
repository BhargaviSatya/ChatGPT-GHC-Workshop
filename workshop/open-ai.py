from openai import OpenAI

# Initialize client directly with your API key
client = OpenAI(api_key="<Add your API Key>")

# Send a simple prompt
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o" for a larger model
    messages=[
        {"role": "system", "content": "You are a helpful research assistant."},
        {"role": "user", "content": "Conduct detailed research on quantum computing — explain its principles, key technologies, and current challenges in 2025."}
    ]
)

# Print the model’s reply
print(response.choices[0].message.content)