import json

# Importar de um arquivo
with open('json/imobiliaria.json', encoding='utf-8') as json_file:
    parsed_data = json.load(json_file)

imoveis = parsed_data["imobiliaria"]["imoveis"]
id_imovel = 1
for imovel in imoveis:
    print(f"Imóvel {id_imovel}: {imovel['descricao']}")
    id_imovel += 1

print("="*10)

id_selecionado = int(input("INFORME O ID DO IMÓVEL:"))  
imovel = imoveis[id_selecionado - 1]

descricao_da_casa = imovel["descricao"]
proprietario_da_casa = imovel["proprietario"]
telefones = proprietario_da_casa.get("telefones") or [proprietario_da_casa.get("telefone", "Não informado")]
email_do_proprietario = proprietario_da_casa["email"]
endereco_do_imovel = imovel["endereco"]
caracteristicas_do_imovel = imovel["caracteristicas"]
valor_do_imovel = imovel["valor"]


print("="*10)
print("Descrição geral:")
print(" ° Descrição do Imovel:", descricao_da_casa)
print(" ° Proprietário(a):", proprietario_da_casa['nome'])

for telefone in telefones:
    print(" ° Telefone:" ,telefone )

print(" ° Email:", email_do_proprietario )
print("")

print("Endereço do imovel:")
print(f" °  Endereço da Rua: {endereco_do_imovel['rua']}")
print(f" °  Endereço do Bairro: {endereco_do_imovel['bairro']}")
print(f" °  Endereço da Cidade: {endereco_do_imovel['cidade']}")
print(f" °  Número do imovel: {endereco_do_imovel['numero'] if endereco_do_imovel['numero'] is not None else 'N/A'}")
print("")

print("Características dentro do imovel:")
print(f" ° Características do Tamanho do Imovel : {caracteristicas_do_imovel ['tamanho']} m²")
print(f" ° Características do Número do Quartos: {caracteristicas_do_imovel ['numQuartos']}")
print(f" ° Características do Número do Banheiros: {caracteristicas_do_imovel ['numBanheiros']}")
print("")

print("Valor geral do Imovel:", valor_do_imovel )