import requests
from getpass import getpass
import json

def autenticar(api_url):
    user = input("user: ")
    password = getpass()

    data = {"username":user,"password":password}

    response = requests.post(api_url+"v2/autenticacao/token/", json=data)
    print(response.json())
    return response.json()["access"]

def main():
    api_url = "https://suap.ifrn.edu.br/api/"

    with open('suap_keys.json', 'r') as file:
        try: 
            data= json.load(file)
            print(data)
        except json.decoder.JSONDecodeError:
            data = {}
            data['token'] = autenticar (api_url)
            json.dump(data,file)

    
    token = data['token'] 
    headers = {
        "Authorization": f'Bearer {token}'
    }

    print(headers)

    response = requests.get(api_url+"v2/minhas-informacoes/meus-dados/", headers=headers)

    print(response.text)
    print(response)


if __name__== '__main__':
    main()






