import requests
import xml.dom.minidom

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
headers = {'Content-Type': 'text/xml; charset=utf-8'}

def get_info(function_name, country_code):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <{function_name} xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{country_code}</sCountryISOCode>
            </{function_name}>
        </soap:Body>
    </soap:Envelope>"""
    response = requests.post(url, headers=headers, data=payload)
    return xml.dom.minidom.parseString(response.text)


capital = get_info("CapitalCity", "NZ").getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
print(f"Capital da Nova Zelândia: {capital}")

currency = get_info("CountryCurrency", "JP").getElementsByTagName('m:sName')[0].firstChild.nodeValue
print(f"Moeda do Japão: {currency}")

country_name = get_info("CountryName", "BR").getElementsByTagName('m:CountryNameResult')[0].firstChild.nodeValue
print(f"Nome do país (BR): {country_name}")

country_name = get_info("CountryName", "US").getElementsByTagName('m:CountryNameResult')[0].firstChild.nodeValue
print(f"Nome do país (US): {country_name}")