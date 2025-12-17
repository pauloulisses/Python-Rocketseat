import requests

url = "https://www.w3schools.com/python/python_datetime.asp"

resposta = requests.get(url)

print(f"Solicitação HTTP para {url} retornou o status{resposta.status_code}")