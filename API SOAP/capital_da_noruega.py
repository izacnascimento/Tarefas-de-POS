import requests
from xml.dom.minidom import parseString
import zeep

# Parte 1: Capital da Noruega (NO)
def capital_da_noruega(country):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country}</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
                </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    capitaldanoruega = context.getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
    return capitaldanoruega


def number_to_text(num):
    number_words = {
        212: "two hundred twelve",
        213: "two hundred thirteen",
        214: "two hundred fourteen",
        215: "two hundred fifteen",
        216: "two hundred sixteen",
        217: "two hundred seventeen",
        218: "two hundred eighteen",
        219: "two hundred nineteen",
        220: "two hundred twenty",
        221: "two hundred twenty-one",
        222: "two hundred twenty-two",
        223: "two hundred and twenty three"
    }
    return number_words.get(num, "Numero não esta na tabela!")

if __name__ == "__main__":
    # Parte 2: Converter número por extenso em inglês
    numero_convertido = int(input("Informe um número de 212 a 223 para converter por extenso: "))
    numero_por_extenso = number_to_text(numero_convertido)
    print(f"O número {numero_convertido} por extenso em inglês é: {numero_por_extenso}")