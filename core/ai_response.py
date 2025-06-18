import requests

def get_ai_response(prompt):
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful and witty assistant. Speak like Jarvis from Iron Man."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Apologies, I encountered an issue while trying to respond."
