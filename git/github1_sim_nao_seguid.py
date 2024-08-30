import requests
from requests.auth import HTTPBasicAuth

# Configurações de autenticação (use o token de acesso pessoal aqui)
token = '' # Substitua pelo seu token de acesso pessoal do GitHub

# Cabeçalhos de autenticação
headers = {
    "Authorization": f"token {token}"
}

# Função para listar seguidores
def listartodososseguidores():
    response = requests.get('https://api.github.com/user/followers', headers=headers)

    if response.status_code == 200:
        seguidores = response.json()
        if seguidores:
            print("Seguidores:")
            for seguidor in seguidores:
                print(f'- {seguidor["login"]}')
        else:
            print("Nenhum seguidor encontrado.")
    else:
        print(f"Erro ao listar seguidores: {response.status_code} - {response.text}")

# Função para seguir um usuário
def seguir_um_individuo(user):
    response = requests.put(f'https://api.github.com/user/following/{user}', headers=headers)

    if response.status_code == 204:
        print(f'Seguindo {user} com sucesso!')
    elif response.status_code == 404:
        print(f"Usuário {user} não encontrado.")
    else:
        print(f"Erro ao seguir {user}: {response.status_code} - {response.text}")

# Função para parar de seguir um usuário
def parardeseguir_individuo(user):
    response = requests.delete(f'https://api.github.com/user/following/{user}', headers=headers)

    if response.status_code == 204:
        print(f'Parou de seguir {user} com sucesso!')
    elif response.status_code == 404:
        print(f"Usuário {user} não encontrado.")
    else:
        print(f"Erro ao parar de seguir {user}: {response.status_code} - {response.text}")

# Função principal
def menuprincipal():
    while True:
        print("\nEscolha uma opção:")
        print("1. Listar seguidores")
        print("2. Seguir um usuário")
        print("3. Parar de seguir um usuário")
        print("4. Sair")
        
        escolha = input("Digite o número da opção: ")
        
        if escolha == '1':
            listartodososseguidores()
        elif escolha == '2':
            user = input("Digite o usuário para seguir: ")
            seguir_um_individuo(user)
        elif escolha == '3':
            user = input("Digite o usuário para parar de seguir: ")
            parardeseguir_individuo(user)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menuprincipal()
