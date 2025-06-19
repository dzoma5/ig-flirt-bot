import requests
import random

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {"Authorization": "Bearer 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"}

PROMPTI = [
    "Napiši duhovit, samouveren i flert komentar za Instagram meme o lošim dejtovima.",
    "Napiši komentar koji je smešan i koketan, kao da se zezaš s osobom koja je objavila meme.",
    "Flertuj kroz sarkazam u komentaru na meme o vezama.",
    "Napiši kao da si zavodnik koji koristi meme kao izgovor za upad.",
    "Napiši zavodnički komentar ispod slike gde neko kuka o singl životu."
]

def generate_comment():
    prompt = random.choice(PROMPTI)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 50,
            "temperature": 0.8,
            "top_p": 0.95,
        }
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    output = response.json()
    return output[0]["generated_text"]

if __name__ == "__main__":
    comment = generate_comment()
    print("\n📢 AI komentar za Instagram:")
    print(comment)
