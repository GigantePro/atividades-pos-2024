import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username": user, "password": password}
response = requests.post(api_url + "v2/autenticacao/token/", json=data)
token = response.json().get("access")

headers = {"Authorization": f"Bearer {token}"}

ano_letivo = input('Digite o ano letivo: ')
periodo_letivo = input('Digite o período letivo: ')
boletim_url = f"{api_url}v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/"
response = requests.get(boletim_url, headers=headers)

for data in response.json():
    print(f"Disciplina: {data['disciplina']}")
    for i in range(1, 5):
        print(f"Nota etapa {i} - {data[f'nota_etapa_{i}']['nota']}")
    print(f"Média final - {data['media_final_disciplina']}")
    print(f"Número de faltas - {data['numero_faltas']}\n")