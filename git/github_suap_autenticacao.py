import requests
from getpass import getpass
import json
import os
from prettytable import PrettyTable

def autenticacao_do_boletim_suap(api_url):
    print("Por favor, digite o usuário e senha para autenticação.")
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")

    dados = {"username": usuario, "password": senha}
    resposta = requests.post(api_url + "v2/autenticacao/token/", json=dados)

    if resposta.status_code == 200:
        return resposta.json()["access"]
    else:
        print("Falha na autenticação:", resposta.status_code, resposta.text)
        return None

def Obtem_o_boletim_suap(api_url, cabecalhos, ano_letivo, periodo_letivo):
    url = f"{api_url}v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/"
    resposta = requests.get(url, headers=cabecalhos)

    if resposta.status_code == 200:
        return resposta.json()
    elif resposta.status_code == 401:
        print("Token inválido ou expirado. Reautenticando...")
        return "INVALID_TOKEN"
    else:
        print("Erro ao obter o boletim:", resposta.status_code, resposta.text)
        return None

def formatacao_do_boletim_suap(boletim):
    tabela = PrettyTable()
    tabela.field_names = ["Disciplina", "Nota Unidade 1", "Nota Unidade 2", "Nota Unidade 3", "Nota Unidade 4", "Situação"]

    for disciplina in boletim:
        nome_disciplina = disciplina.get("disciplina", "N/A")
        notas = [
            disciplina.get("nota_unidade_1", "N/A"),
            disciplina.get("nota_unidade_2", "N/A"),
            disciplina.get("nota_unidade_3", "N/A"),
            disciplina.get("nota_unidade_4", "N/A"),
        ]
        situacao = disciplina.get("situacao", "N/A")
        tabela.add_row([nome_disciplina] + notas + [situacao])

    print(tabela)

def menu():
    api_url = "https://suap.ifrn.edu.br/api/"
    
    ano_letivo = input("Ano Letivo: ")
    periodo_letivo = input("Período Letivo: ")

    token = None

    if os.path.exists('suap_keys.json'):
        with open('suap_keys.json', 'r') as arquivo:
            try:
                dados = json.load(arquivo)
                token = dados.get('token')
            except json.decoder.JSONDecodeError:
                token = None

    if not token:
        token = autenticacao_do_boletim_suap(api_url)
        if token:
            with open('suap_keys.json', 'w') as arquivo:
                json.dump({"token": token}, arquivo)
        else:
            return  # Interrompe a execução se não conseguir autenticar

    cabecalhos = {
        "Authorization": f'Bearer {token}'
    }

    boletim = Obtem_o_boletim_suap(api_url, cabecalhos, ano_letivo, periodo_letivo)

    if boletim == "INVALID_TOKEN":
        token = autenticacao_do_boletim_suap(api_url)
        if token:
            with open('suap_keys.json', 'w') as arquivo:
                json.dump({"token": token}, arquivo)
            cabecalhos = {
                "Authorization": f'Bearer {token}'
            }
            boletim = Obtem_o_boletim_suap(api_url, cabecalhos, ano_letivo, periodo_letivo)
        else:
            return

    if boletim:
        formatacao_do_boletim_suap(boletim)

if __name__ == '__main__':
    menu()
