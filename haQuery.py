from configparser import SafeConfigParser
import warnings
import requests
from getSat import getSat, makelist
from getIri import getIri
from IridiumFlare import IridiumFlare
from analysis import iriAnalysis


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # Reading ini config
    config = SafeConfigParser()
    config.read('config.ini')
    haBaseUrl = config.get('main', 'baseUrl')
    satQuery = config.get('main', 'satQuery')
    iriQuery = config.get('main', 'iriQuery')
    satIdList = config.get('satellite', 'id')
    satNameList = config.get('satellite', 'name')
    loc_lat = config.getfloat('observatory', 'latitude')
    loc_lng = config.getfloat('observatory', 'longitude')
    loc_alt = config.getfloat('observatory', 'altitude')
    loc_loc = config.get('observatory', 'name')
    loc_tz = config.get('observatory', 'timezone')
    ngtEnd = config.get('analysis', 'nightEnd')
    dwnEnd = config.get('analysis', 'dawnEnd')
    mrnEnd = config.get('analysis', 'morningEnd')
    aftEnd = config.get('analysis', 'afternoonEnd')
    dskEnd = config.get('analysis', 'duskEnd')
    magCut = config.getfloat('analysis', 'magCut')
    altCut = config.getfloat('analysis', 'altCut')
    # Define some constant
    loc = {"lat": str(loc_lat), "lng": str(loc_lng), "loc": str(loc_loc),
           "alt": str(loc_alt), "tz": str(loc_tz)}
    headerUA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) ' +
                'Gecko/20100101 Firefox/40.0'}
    # Parsing satellite id list
    satList = map(int, satIdList.split(','))
    satName = satNameList.split(',')
    # Get cookie by getting home page
    s = requests.Session()
    responce = s.get(haBaseUrl, headers=headerUA)
    # Get satellites data
    for eachId, eachName in zip(satList, satName):
        satTable = getSat(eachId, loc, s, haBaseUrl, satQuery, header=headerUA)
        a = makelist(satTable)
    iriTable = getIri(loc, s, haBaseUrl, iriQuery, header=headerUA)
    iriList = makelist(iriTable)
    iriFlareList = []
    for each in iriList:
        iriFlare = IridiumFlare(each)
        iriFlareList.append(iriFlare)
        iriFlare.timeTagging(ngtEnd, dwnEnd, mrnEnd, aftEnd, dskEnd)
        iriFlare.magTagging(magCut)
        iriFlare.altTagging(altCut)
    iriText = iriAnalysis(iriFlareList)
    print(iriText)
