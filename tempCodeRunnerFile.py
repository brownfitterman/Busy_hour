    # insertnumber = 500
    # for n in range(int(len(updateRecords)/insertnumber)+1):
    #     start = (n + 1) * insertnumber
    #     print(len(updateRecords[n * insertnumber :start]))
    #     headers = {'Content-Type': 'application/json',
    #                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36",
    #                "Accept-Encoding": "*",
    #                "Connection": "keep-alive", "Accept": "*/*"}
    #     response = re.post("http://nightlife.cubesservices.com/api/v1/Place/UpdateCurrentPopularity",json=updateRecords[n * insertnumber :start], headers=headers, timeout=20 *60)
    #     try:
    #         print(response.json())
    #     except:
    #         pass
    # print("Data  inserted to  df ")