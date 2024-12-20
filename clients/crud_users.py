import requests

class UsersAPIWrapper:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/users"

    def create(self, user_data):
        response = requests.post(self.base_url, json=user_data)
        return response.json()

    def read(self, user_id):
        response = requests.get(f"{self.base_url}/{user_id}")
        return response.json()

    def update(self, user_id, user_data):
        response = requests.patch(f"{self.base_url}/{user_id}", json=user_data)
        return response.json()

    def delete(self, user_id):
        response = requests.delete(f"{self.base_url}/{user_id}")
        return response.status_code

api = UsersAPIWrapper()

print('1. Criar')
print('2. Ler')
print('3. Atualizar')
print('4. Deletar')

esc = int(input('O que deseja fazer? '))

if esc == 1:
    username = input('Digite o username: ')
    new_user = {
        "name": username,
        "username": username,
        "email": "jaosja@gmail.com"
    }
    response = api.create(new_user)
    print(f"Usuário cadastrado: {response}")

elif esc == 2:
    user_id = int(input('Digite o ID do usuário: '))
    response = api.read(user_id)
    print(f"Usuário: {response}")

elif esc == 3:
    user_id = int(input('Digite o ID do usuário: '))
    username = input('Digite o novo username: ')
    user_data = {"username": username}
    response = api.update(user_id, user_data)
    print(f"Usuário atualizado: {response}")

elif esc == 4:
    user_id = int(input('Digite o ID do usuário: '))
    status_code = api.delete(user_id)
    print(f"Delet concluído! Status: {status_code}")