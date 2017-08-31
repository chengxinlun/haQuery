import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def getSat(satid, loc, s, haBaseUrl, satQuery, header=None):
    payload = {"satid": str(satid), "lat": loc["lat"], "lng": loc["lng"],
               "loc": loc["loc"], "alt": loc["alt"], "tz": loc["tz"]}
    responce = s.get(urljoin(haBaseUrl, satQuery), params=payload,
                     headers=header)
    parser = BeautifulSoup(responce.text)
    table = parser.findAll("table", class_="standardTable")
    return str(table)


def delEmp(strList):
    return filter(None, strList)


def makelist(tableStr):
    table = BeautifulSoup(tableStr)
    allrows = table.findAll('tr')
    resList = []
    for each in allrows:
        allCols = each.findAll('td')
        colList = []
        for eachCol in allCols:
            colList.extend(delEmp(re.findall(r'>(.*?)<', str(eachCol))))
        resList.append(colList)
    return list(delEmp(resList))
