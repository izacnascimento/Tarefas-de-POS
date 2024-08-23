import requests
from requests.auth import HTTPBasicAuth

user = input("user: ")
password = "g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"

  
response = requests.patch('https://api.github.com/user/followers?per_page=60',
            auth = HTTPBasicAuth('izacnascimento', password))


seguidores = response.json()

for seguidor in seguidores:
    print(seguidor['login'])

print(response.text)
print(response)