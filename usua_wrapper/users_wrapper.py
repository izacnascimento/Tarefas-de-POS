import requests

class UsersWrapper:
    api_url = "https://jsonplaceholder.typicode.com/users/"

    def listar_usuarios(self):
        response = requests.get(self.api_url)
        return response.json()

    def criar_usuario(self, user_data):
        response = requests.post(self.api_url, json=user_data)
        return response.status_code

    def atualizar_usuario(self, id, user_data):
        url = f"{self.api_url}{id}"
        response = requests.put(url, json=user_data)
        return response.status_code

    def deletar_usuario(self, id):
        url = f"{self.api_url}{id}"
        response = requests.delete(url)
        return response.status_code

if __name__ == "__main__":
    users_wrapper = UsersWrapper()

    # MENU PRINCIPAL
    print("1 - Listar os usuários!")
    print("2 - Criar um usuário!")
    print("3 - Atualizar um usuário!")
    print("4 - Deletar um usuário!")
    opcao = int(input())


    # OPÇÂO DE LISTAR TODOS OS USUÁRIO
    if opcao == 1:
        usuarios = users_wrapper.listar_usuarios()
        for usuario in usuarios:
            print(f"{usuario['id']} - {usuario['name']}")


     # OPÇÂO DE CRIAR UM USUÁRIO
    elif opcao == 2:
        usuar_nome = input("DIGITE O NOME DO USUÁRIO:")
        usuar_email = input("INFORME O EMAIL DO USUÁRIO: ")
        usuar_telefone = input("INFORME O TELEFONE DO USUÁRIO:")
        user_data = {
            "name": usuar_nome,
            "email": usuar_email,
            "telefone": usuar_telefone
        }
        response = users_wrapper.criar_usuario(user_data)

        if response == 201:
            print("USUÁRIO FOI CRIADO COM SUCESSO, TUDO OK!")
        else:
            print("DEU FALHAR AO TENTAR CRIAR UM USUÁRIO!")


    # OPÇÂO DE ATUALIZAR UM USUÁRIO
    elif opcao == 3:
        id_usuario = input("INFORME O ID DO USUÁRIO: ")
        usua_nome = input("INFORME O SEU NOME: ")
        usua_email = input("INFORME O SEU EMAIL: ")
        usua_telefone = input("INFORME O SEU TELEFONE: ")
        usua_cidade = input("INFORME A SUA CIDADE: ")
        user_data = {
            "nome": usua_nome,
            "usuario": id_usuario,
            "email": usua_email,
            "telefone": usua_telefone,
            "endereco": {
                "cidade": usua_cidade
            }
        }

        response = users_wrapper.atualizar_usuario(id_usuario, user_data)
        if response == 200:
            print("USUÁRIO FOI ATUALIZANDO COM SUCESSO, TUDO OK!")
        else:
            print("DEU FALHAR AO TENTAR ATUALIZAR UM USUÁRIO!")


    # OPÇÂO DE DELETAR UM USUÁRIO
    elif opcao == 4:
        id_usuario = input("INFORME O ID DO USUÁRIO: ")
        response = users_wrapper.deletar_usuario(id_usuario)
        if response == 200:
            print("USUÁRIO FOI DELETANDO COM SUCESSO, TUDO OK!")
        else:
            print("DEU FALHAR AO TENTAR DELETAR UM USUÁRIO!")

