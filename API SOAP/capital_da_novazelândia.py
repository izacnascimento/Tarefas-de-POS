import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

def capital_novazelândia (country):
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
    capitalnovazelândia = context.getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
    return capitalnovazelândia

# Testando com outras três funções da API
def nome_pais_novaZelândia(country):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country}</sCountryISOCode>
                    </CountryName>
                </soap:Body>
                </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    nome_paisnovazelândia = context.getElementsByTagName('m:CountryNameResult')[0].firstChild.nodeValue
    return nome_paisnovazelândia

def moeda_pais_novazelândia(country):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country}</sCountryISOCode>
                    </CountryCurrency>
                </soap:Body>
                </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    moedadopais = context.getElementsByTagName('m:CountryCurrencyResult')[0].getElementsByTagName('m:sISOCode')[0].firstChild.nodeValue
    return moedadopais

def codigo_tel_novazelândia(country):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country}</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
                </soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    codigo_teldopais = context.getElementsByTagName('m:CountryIntPhoneCodeResult')[0].firstChild.nodeValue
    return  codigo_teldopais

novazelândia = "NZ"

# Obtendo a capital da Nova Zelândia
capital = capital_novazelândia(novazelândia)
print(f"A capital da Nova Zelândia é: {capital}")

# Testando outras três funções da API
nome_pais = nome_pais_novaZelândia(novazelândia)
moeda = moeda_pais_novazelândia(novazelândia)
codigo_telefone = codigo_tel_novazelândia(novazelândia)

print(f"Nome do país: {nome_pais}")
print(f"Moeda do país: {moeda}")
print(f"Código de telefone do país: +{codigo_telefone}")
