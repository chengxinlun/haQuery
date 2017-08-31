from bs4 import BeautifulSoup
from urllib.parse import urljoin


def getIri(loc, s, haBaseUrl, iriQuery, header=None):
    payload = {"lat": loc["lat"], "lng": loc["lng"],
               "loc": loc["loc"], "alt": loc["alt"], "tz": loc["tz"]}
    responce = s.get(urljoin(haBaseUrl, iriQuery), params=payload,
                     headers=header)
    parser = BeautifulSoup(responce.text)
    table = parser.findAll("table", class_="standardTable")
    return str(table)
