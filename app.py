import time
import requests

def fetch_data():
    url = "https://apicotacaoovos.onrender.com/api/eggs_online"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Dados recebidos:", data)
        else:
            print(f"Falha ao buscar dados. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(60)  # Espera 1 minuto antes de fazer a próxima requisição
