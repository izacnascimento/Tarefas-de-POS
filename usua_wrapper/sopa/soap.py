import requests
from xml.dom.minidom import parseString
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

country = input('Digite o codigo do Pais:')
funcao = "Country"
# XML estruturado
payload = """<?xml version="1.0" encoding="utf-8"?>
			<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
			<soap:Body>
				< xmlns="http://www.oorsprong.org/websamples.countryinfo">
				<sCountryISOCode></sCountryISOCode>
				</>
				</soap:Body>
			</soap:Envelope>"""


# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)



# imprime a resposta
context = parseString(response.text)
print(context.documentElement.getElementsByTagName('m: sName')[0].firstChild.nodeValue)