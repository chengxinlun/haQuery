import warnings
import requests
from getSat import getSat, makelist


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    # Define some constant
    haBaseUrl = 'http://www.heavens-above.com'
    satQuery = 'PassSummary.aspx'
    loc = {"lat": "40.01", "lng": "116.3295", "loc": "Beijing", "alt": "43",
           "tz": "ChST"}
    issId = 25544
    headerUA = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) ' +
                'Gecko/20100101 Firefox/40.0'}
    # Get cookie by getting home page
    s = requests.Session()
    responce = s.get(haBaseUrl, headers=headerUA)
    # Get ISS data
    issTable = getSat(issId, loc, s, haBaseUrl, satQuery, header=headerUA)
    a = makelist(issTable)
    print(a)
