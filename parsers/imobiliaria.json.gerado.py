from xml.dom.minidom import parse
import json

# 1) PARSE DO ARQUIVO IMOBILIARIA.XML
dom = parse("xml_xsd/imobiliaria/imobiliaria.xml")
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName("imovel")

# 2) CRIE UMA VARIAVEL DATA QUE VAI LISTA OU ARMAZENAR TODOS OS DADOS
data = {"imoveis": []}

# 3) RELATORIO GERAL DA ESTRUTURA DO IMOVEL XML
for imovel in imoveis:
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    proprietario = imovel.getElementsByTagName("proprietario")[0]
    nome_proprietario = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue
    
    # 4) 'OS DADOS IMPORTANTE DO PROPRIETÁRIO'
    telefones_proprietario = proprietario.getElementsByTagName("telefone")
    telefones = [telefone.firstChild.nodeValue for telefone in telefones_proprietario]
    emails_proprietario = proprietario.getElementsByTagName("email")
    emails = [email.firstChild.nodeValue for email in emails_proprietario]
    
    # 5) 'O ENDEREÇO DO IMOVEL'
    endereco = imovel.getElementsByTagName("endereco")[0]
    rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue
    
    numero_do_imovel = imovel.getElementsByTagName("numero")
    numero = numero_do_imovel[0].firstChild.nodeValue.strip() if numero_do_imovel and numero_do_imovel[0].firstChild else None


    # 6) 'TODAS AS CARACTERISTICA RELACIONANDO DENTRO DA CASA'
    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = float(caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue.split()[0])
    numQuartos = int(caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue)
    numBanheiros = int(caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue)

    valor = float(imovel.getElementsByTagName("valor")[0].firstChild.nodeValue)

    # 7) 'O MANUAL DA ESTRUTURA DO ARQUIVO IMOBILIARIA.JSON'
    data["imoveis"].append({
        "descricao": descricao,
        "proprietario": {
            "nome": nome_proprietario,
            "telefones": telefones,
            "emails": emails
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    })

#  8) 'GERANDO O ARQUIVO IMOBILIARIA.JSON'
with open("parsers/imobiliaria.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

print("Arquivo imobiliaria.json Gerado com sucesso!")