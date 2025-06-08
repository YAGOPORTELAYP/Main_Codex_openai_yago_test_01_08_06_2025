import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ollama(prompt: str) -> str:
    payload = {"model": "llama3", "prompt": prompt}
    resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
    resp.raise_for_status()
    # Ollama streams chunks separated by newlines. Take the 'response' field from each.
    answer = "".join(chunk.get("response", "") for chunk in resp.json())
    return answer.strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python chatbot.py 'your question'")
        sys.exit(1)
    question = sys.argv[1]
    print(ask_ollama(question))


if __name__ == "__main__":
    main()
