import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/"
LOGIN_URL = f"{BASE_URL}token/"
TECNOS_URL = f"{BASE_URL}tecnologias/"
TOKEN_FILE = "token.json"  # Arquivo para armazenar o token

def get_token(username, password):
    response = requests.post(LOGIN_URL, json={"username": username, "password": password})
    if response.status_code == 200:
        token = response.json().get("access")
        print("Token gerado:", token)  # Adicionando para depuração
        with open(TOKEN_FILE, "w") as f:
            json.dump({"token": token}, f)
        return token
    print("Erro ao autenticar:", response.json())
    return None


def load_token():
    try:
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)
            return data["token"]
    except FileNotFoundError:
        return None

def get_tecnologias():
    token = load_token()
    if not token:
        print("Token não encontrado. Faça login primeiro.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(TECNOS_URL, headers=headers)
    return response.json()

if __name__ == "__main__":
    username = "victor"
    password = "Victo2025!"

    token = load_token()  # Tenta carregar o token salvo
    if not token:  # Se não existir, faz login e salva
        token = get_token(username, password)

    if token:
        tecnologias = get_tecnologias()
        print("Tecnologias disponíveis:", tecnologias)
    else:
        print("Falha ao obter token.")
