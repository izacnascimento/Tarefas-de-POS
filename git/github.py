import requests
from requests.auth import HTTPBasicAuth

user = input("user: ")
password = "g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"

user = input("Digite o login do usuario para seguir: ")
user = input("Digite o login do usuario para parar de seguir: ")
response = requests.put('https://api.github.com/user/following/{user}',
            auth = HTTPBasicAuth('izacnascimento', password))


seguidores = response.json()

for seguidor in seguidores:
    print(seguidor['login'])

print(response.status_code)