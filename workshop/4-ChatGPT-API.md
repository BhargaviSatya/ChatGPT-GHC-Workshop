# 🧠 OpenAI API Python Example (API Key in Code)

This project demonstrates a simple way to integrate with the **OpenAI API** and run a small prompt using Python — with your **API key set directly in the script**.

---

## 🚀 Setup

### 1. Install Dependencies
Make sure you have Python 3.8+ installed, then install the official OpenAI library:
```bash
pip install openai
```

---

## 💬 Example Usage

Here’s a minimal Python script that sends a chat prompt and prints the response.  
💡 *Replace `"your_api_key_here"` with your actual OpenAI API key.*

```python
from openai import OpenAI

# Initialize client directly with your API key
client = OpenAI(api_key="your_api_key_here")

# Send a simple prompt
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o" for a larger model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short haiku about the moon."}
    ]
)

# Print the model’s reply
print(response.choices[0].message.content)
```

---

## 🧾 Example Output
```
Silver moonlight glows,  
Silent whispers through the trees,  
Dreams drift on cool breeze.
```

---

## 📘 Documentation

- **Chat Completions Guide:** [https://platform.openai.com/docs/guides/chat-completions](https://platform.openai.com/docs/guides/chat-completions)
- **Chat Create API Reference:** [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create)

---

## ⚙️ Optional: Run Asynchronously

If you need to send many prompts efficiently, use the async version:

```python
import asyncio
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI(api_key="your_api_key_here")
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Write a quick poem about the stars."}]
    )
    print(response.choices[0].message.content)

asyncio.run(main())
```

---