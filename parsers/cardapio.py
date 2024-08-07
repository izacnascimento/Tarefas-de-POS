from xml.dom.minidom import parse

dom = parse("xml_xsd/cardapio/Cardapio.xml")
cardapio = dom.documentElement
pratos_cardapio = cardapio.getElementsByTagName("prato")

for prato in pratos_cardapio:
    
    prato_id_cardapio = prato.getAttribute("id")
    elemento_nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f" Prato {prato_id_cardapio }: {elemento_nome}")  
 

prato_id = int(input("DIGITE O ID DO PRATO/CARDAPIO: "))
prato = pratos_cardapio [prato_id]

descricao_prato = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue 
elemento_ingredientes = prato.getElementsByTagName("ingrediente")
elemento_ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in elemento_ingredientes]
preco_do_prato = prato.getElementsByTagName("preco")[0].firstChild.nodeValue 
calorias_do_prato = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue 
tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue 

print("="*10)
print(f"Nome do Prato: {elemento_nome}")
print(f"Descrição do Prato: {descricao_prato}")
print(f"Ingredientes:")
print(f"\n".join(elemento_ingredientes))
print(f"Preço do Prato: R${preco_do_prato}")
print(f"Calorias do Prato: {calorias_do_prato} Kilocaloria")
print(f"Tempo de Preparo: {tempoPreparo}")
print("="*10)