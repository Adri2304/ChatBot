import requests

def preguntar_a_gemma2b(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto que responde de forma clara y detallada."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )
    response.raise_for_status()
    data = response.json()
    return data['message']['content']
