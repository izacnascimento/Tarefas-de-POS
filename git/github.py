import requests
from requests.auth import HTTPBasicAuth

user = input("user: ")
password = "g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"

dados = {
    "bio": "Isso foi alterado usado a API"
} 

  
response = requests.patch('https://api.github.com/user',
            auth = HTTPBasicAuth('izacnascimento', password), json=dados)

print(response.status)