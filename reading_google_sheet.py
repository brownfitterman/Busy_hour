from __future__ import print_function
import requests as re
import urllib.request
import urllib.parse
import time
import ssl
import logging
import json
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import random
from google.oauth2 import service_account
from googleapiclient.discovery import build


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1JIsKGiboIPb48RFclyOvQqXMUnnLNhll1s6nhyNzRYY'
SAMPLE_RANGE_NAME = 'Attractions!A2:A'
SERVICE_ACCOUNT_FILE='keys.json'
creds = None
creds=service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
print(result)
values = result.get('values', [])
print(len(values))
values=str(values).replace("[[","[").replace("]]","]").replace("], [",",").replace("['","").replace("','",",").replace("']","").split(",")
print((values))

def job():
    creds=service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)
    values=str(values).replace("[[","[").replace("]]","]").replace("], [",",").replace("['","").replace("','",",").replace("']","").split(",")
    print((values))
    rows=values

    search_url = "http://list.didsoft.com/get?email=rajeshkumardevapp@gmail.com&pass=zxamw8&pid=http1000&showcountry=no&level=3"

    resp = urllib.request.urlopen(urllib.request.Request(url=search_url, data=None))
    data = resp.read().decode('utf-8').split('/*""*/')[0]

    urls = data.split("\n")

    def index_get(array, *argv):
        try:
            for index in argv:
                array = array[index]
            return array
        except (IndexError, TypeError):
            return None
        
  
    def get_it(url):
        try:
            
            USER_AGENT = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/54.0.2840.98 Safari/537.36"}
            params_url = {
            "tbm": "map",
            "tch": 1,
            "hl": "en",
            "q": urllib.parse.quote_plus(url),
            "pb": "!4m12!1m3!1d4005.9771522653964!2d-122.42072974863942!3d37.8077459796541!2m3!1f0!2f0!3f0!3m2!1i1125!2i976"
                "!4f13.1!7i20!10b1!12m6!2m3!5m1!6e2!20e3!10b1!16b1!19m3!2m2!1i392!2i106!20m61!2m2!1i203!2i100!3m2!2i4!5b1"
                "!6m6!1m2!1i86!2i86!1m2!1i408!2i200!7m46!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!"
                "1m3!1e4!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e"
                "10!2b0!3e4!2b1!4b1!9b0!22m6!1sa9fVWea_MsX8adX8j8AE%3A1!2zMWk6Mix0OjExODg3LGU6MSxwOmE5ZlZXZWFfTXNYOGFkWDh"
                "qOEFFOjE!7e81!12e3!17sa9fVWea_MsX8adX8j8AE%3A564!18e15!24m15!2b1!5m4!2b1!3b1!5b1!6b1!10m1!8e3!17b1!24b1!"
                "25b1!26b1!30m1!2b1!36b1!26m3!2m2!1i80!2i92!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i976!1m6!1m2!1i1075!2i0!2m2!"
                "1i1125!2i976!1m6!1m2!1i0!2i0!2m2!1i1125!2i20!1m6!1m2!1i0!2i956!2m2!1i1125!2i976!37m1!1e81!42b1!47m0!49m1"
                "!3b1"
                }
            
            search_url = "https://www.google.de/search?" + "&".join(k + "=" + str(v) for k, v in params_url.items())
            logging.info("searchterm: " + search_url)
            
            proxy_handler = urllib.request.ProxyHandler({'http': random.choice(urls)})
            req = urllib.request.Request(url=search_url, data=None, headers=USER_AGENT)
            opener = urllib.request.build_opener(proxy_handler)
            resp = opener.open(req)
            
            data = resp.read().decode('utf-8').split('/*""*/')[0]
            # print(data)
           
            jend = data.rfind("}")
            # print(jend)
            if jend >= 0:
                data = data[:jend + 1]
            
            jdata = json.loads(data)["d"]

            jdata = json.loads(jdata[4:])
            
            info = index_get(jdata, 0, 1, 0, 14)
            current_popularity = index_get(info, 84, 7, 1)
            if current_popularity == None:
                current_popularity = 0
            print(current_popularity, time.time())
            current_popularitys.append([current_popularity])
            # updateRecords.append({ 'googlePlaceName': url, 'currentpopularity': current_popularity })
            
        except Exception as e:
            print("Unable to get url {} due to {}.".format(url, e.__class__))
            current_popularitys(["N/A"])


    start = time.time()
    current_popularitys=[]
    with PoolExecutor(max_workers=20) as executor:
        for _ in executor.map(get_it, rows):
            pass
    end = time.time()
    print(current_popularitys)
    print("Took {} seconds to pull websites.".format(end - start))
    update=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Attractions!d2',valueInputOption="USER_ENTERED",body={"values":current_popularitys}).execute()

while True:
    try:
        job()
        time.sleep(180)
    except Exception as err:
        print(err)
        break
        print("except")
        pass