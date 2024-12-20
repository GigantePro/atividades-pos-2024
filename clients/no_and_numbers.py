import requests
import xml.dom.minidom

def get_info(function_name, country_code):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <{function_name} xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{country_code}</sCountryISOCode>
            </{function_name}>
        </soap:Body>
    </soap:Envelope>"""
    response = requests.post("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso", headers={'Content-Type': 'text/xml; charset=utf-8'}, data=payload)
    return xml.dom.minidom.parseString(response.text)

def number_to_words(numero):
    url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                <ubiNum>{numero}</ubiNum>
            </NumberToWords>
        </soap:Body>
    </soap:Envelope>"""
    response = requests.post(url, headers={'Content-Type': 'text/xml; charset=utf-8'}, data=payload)
    dom = xml.dom.minidom.parseString(response.text)
    return dom.getElementsByTagName('m:NumberToWordsResult')[0].firstChild.nodeValue



capital = get_info("CapitalCity", "NO").getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
print(f"Capital da Noruega: {capital}")

numero = int(input("digite um número: "))
numeroExtenso = number_to_words(numero)
print(f"O número {numero} por extenso é: {numeroExtenso}")
