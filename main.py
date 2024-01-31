from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/fare-estimate')
async def fare_estimate():
    url = 'https://api.jeenyme.com/taximeter/fare-estimate/v2/?matrix=1&destination_lat=24.7240712&pickup_lng=46.6629288&area_code=RUH&pickup_lat=24.6923948&destination_lng=46.6039167'
    
    try:
        response = requests.get(url,verify=False)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}


@app.get('/get_data')
async def s_data(page_num):
   
    cookies = {
        'GCLB': 'CLKlxa-CpYvcqwE',
        'TiPMix': '51.3812393950678',
        'x-ms-routing-name': 'self',
        'tr-plan-id': '0',
        'tr-plan-name': 'free',
        'tr-experiments-version': '1.14',
        'tipranks-experiments': '%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v2%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v3%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d',
        'tipranks-experiments-slim': 'general_A%3av2%7cgeneral_B%3av3',
        '_gcl_au': '1.1.717755065.1706085664',
        '_gid': 'GA1.2.993209483.1706085664',
        '_hjHasCachedUserAttributes': 'true',
        'FPAU': '1.1.717755065.1706085664',
        '_ce.irv': 'new',
        'cebs': '1',
        'prism_90278194': '4d3b8199-e05b-4589-ae03-e25d09481def',
        '_ce.clock_event': '1',
        '_fbp': 'fb.2.1706085663370.2031937143',
        '_fbp': 'fb.2.1706085663370.2031937143',
        '_hjSessionUser_2550200': 'eyJpZCI6IjJjMzAzNDczLTViZDMtNWJkYS1hMjIyLTA3ODhiNzI3NDU3ZiIsImNyZWF0ZWQiOjE3MDYwODU2NjQzMDksImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_2550200': 'eyJpZCI6ImQxMmFjMjAwLWM4MDctNDc3Mi04ODFlLTkwZDRiYjI1ZWE0OSIsImMiOjE3MDYwODgyNDE3MTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        'rbzid': 't68kT9GlPQvO6nbtLMoF6ufpSQ+BAk+A35nZntiFcF9wlXFaZJALGXVGUHWYLN3jUC25BKyDbH12p1bwEwbMRfgMjfCcTHq9Qgll6ajTcaDrjVDqMPHveFqf+zjso92uMEjH4wtxdv8r2nbBrWt8KAjLd9+o6sDIb8Cqy0wDs0q1Wx0cxrCi6tssuaxKUPQ+fOQBjYmENV/R8Dqgopn/5OLZTlWKlGreNXsxpAVcu3+XoTFFchIUVYSDolED1k2PHgtRG8OeEJnm5vZ8/c3doJMIqg1JdYAcvoFTQLIHhps=',
        'rbzsessionid': '05547f402b4dce9fa5e8acbf3f8ff3bd',
        '_ce.clock_data': '-274%2C%2C1%2C24e87e5f156ab48c5bb559e4c1652234',
        'g_state': '{"i_p":1706096310804,"i_l":1}',
        '_ga_FFX3CZN1WY': 'GS1.1.1706088237.2.1.1706089119.0.0.0',
        '_ga': 'GA1.2.1554162218.1706085664',
        '_gat_UA-38500593-6': '1',
        'cebsp_': '4',
        '_ce.s': 'v~a0cac2a0572ef79db30cd2663826280d8abaf091~lcw~1706089122987~lva~1706085665570~vpv~0~v11.fhb~1706085666836~v11.lhb~1706089122410~v11.cs~435987~v11.s~50bb0db0-ba9a-11ee-b610-6db5290fb887~v11.sla~1706089123534~lcw~1706089123535',
    }

    headers = {
        'authority': 'www.tipranks.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'GCLB=CLKlxa-CpYvcqwE; TiPMix=51.3812393950678; x-ms-routing-name=self; tr-plan-id=0; tr-plan-name=free; tr-experiments-version=1.14; tipranks-experiments=%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v2%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v3%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d; tipranks-experiments-slim=general_A%3av2%7cgeneral_B%3av3; _gcl_au=1.1.717755065.1706085664; _gid=GA1.2.993209483.1706085664; _hjHasCachedUserAttributes=true; FPAU=1.1.717755065.1706085664; _ce.irv=new; cebs=1; prism_90278194=4d3b8199-e05b-4589-ae03-e25d09481def; _ce.clock_event=1; _fbp=fb.2.1706085663370.2031937143; _fbp=fb.2.1706085663370.2031937143; _hjSessionUser_2550200=eyJpZCI6IjJjMzAzNDczLTViZDMtNWJkYS1hMjIyLTA3ODhiNzI3NDU3ZiIsImNyZWF0ZWQiOjE3MDYwODU2NjQzMDksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2550200=eyJpZCI6ImQxMmFjMjAwLWM4MDctNDc3Mi04ODFlLTkwZDRiYjI1ZWE0OSIsImMiOjE3MDYwODgyNDE3MTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; rbzid=t68kT9GlPQvO6nbtLMoF6ufpSQ+BAk+A35nZntiFcF9wlXFaZJALGXVGUHWYLN3jUC25BKyDbH12p1bwEwbMRfgMjfCcTHq9Qgll6ajTcaDrjVDqMPHveFqf+zjso92uMEjH4wtxdv8r2nbBrWt8KAjLd9+o6sDIb8Cqy0wDs0q1Wx0cxrCi6tssuaxKUPQ+fOQBjYmENV/R8Dqgopn/5OLZTlWKlGreNXsxpAVcu3+XoTFFchIUVYSDolED1k2PHgtRG8OeEJnm5vZ8/c3doJMIqg1JdYAcvoFTQLIHhps=; rbzsessionid=05547f402b4dce9fa5e8acbf3f8ff3bd; _ce.clock_data=-274%2C%2C1%2C24e87e5f156ab48c5bb559e4c1652234; g_state={"i_p":1706096310804,"i_l":1}; _ga_FFX3CZN1WY=GS1.1.1706088237.2.1.1706089119.0.0.0; _ga=GA1.2.1554162218.1706085664; _gat_UA-38500593-6=1; cebsp_=4; _ce.s=v~a0cac2a0572ef79db30cd2663826280d8abaf091~lcw~1706089122987~lva~1706085665570~vpv~0~v11.fhb~1706085666836~v11.lhb~1706089122410~v11.cs~435987~v11.s~50bb0db0-ba9a-11ee-b610-6db5290fb887~v11.sla~1706089123534~lcw~1706089123535',
        'referer': 'https://www.tipranks.com/screener/stocks',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'sortBy': '1',
        'sortDir': '2',
        'page': page_num,
        'pageSize': '50',
        'country': 'us',
        'method': 'screener',
        'isPrimary': 'true',
        'exchange': [
            'xnas',
            'xnys',
            'arcx',
            'xase',
            'bats',
        ],
    }

    response = requests.get('https://www.tipranks.com/api/stocks/screener', params=params, cookies=cookies, headers=headers,verify=False)

    return response.json()

@app.get('/stock_data')
async def get_stock_data(symbol):
  

    cookies = {
        'GCLB': 'CJiS14vHsqS8cg',
        'tr-experiments-version': '1.14',
        'tipranks-experiments': '%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v4%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v4%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d',
        'tipranks-experiments-slim': 'general_A%3av4%7cgeneral_B%3av4',
        'rbzsessionid': '497a17705398d1588cad843a0e929bc9',
        'FPAU': '1.2.874120930.1705841850',
        '_fbp': 'fb.2.1705841849062.590562194',
        '_fbp': 'fb.2.1705841849062.590562194',
        '_gcl_au': '1.1.1070310577.1705841851',
        '_ce.irv': 'new',
        'cebs': '1',
        'prism_90278194': '3d912e60-8289-4304-945e-9376eb7e5e72',
        'g_state': '{"i_l":0}',
        'token': 'a0a1dcd179b1bb63bf838e7d15d510030604a18f',
        'user': 'purushottamd.16@gmail.com,Purushottam Deshpande,',
        'loginType': 'login',
        'tr-plan-id': '1',
        'tr-plan-name': 'basic',
        'tr-uid': '7AE484BBD73059107360EB9C950B6753',
        'rbzid': 'KnVq6vNn1X+rG2SNL8Y1ck+SYQZ+SBmQWgMDWt1konHREG7vij3hpp+woddQZQzBzvd93RFupauqYuJZJNnNPDdUPU4WRDwzeSTkIGD2iZzxHEwx5v4iWT1f4avgM0PW8qunxFcukhZmr2WdacVgo5snb5WoOmKiqWJW8n+KEVwiJgq1Qddmo6jLWIhZT2kF2R385cJLlxE0kGrKijYY5OdZA5GT3afFBYIcBo4h2zpo1GZSG9/ZGk7K48n/H7kqaOcRmw1GRvbjeug+neCz6gCEM88Cg167O8tTWoUm53Q=',
        'TiPMix': '68.69880258033942',
        'x-ms-routing-name': 'self',
        'IC_ViewCounter_www.tipranks.com': '1',
        '_ga': 'GA1.1.1570744259.1705841849',
        '__gads': 'ID=04056718fbfc5622:T=1705841850:RT=1706444413:S=ALNI_MatpluSFD75Yiwo41vvfhpZ59Cmtw',
        '__gpi': 'UID=00000cfbce05c9a0:T=1705841850:RT=1706444413:S=ALNI_MahPg_zSo-hlIvxEssMZ6ns2BqYbA',
        '_ce.clock_event': '1',
        '_ce.clock_data': '-21%2C2.51.77.139%2C1%2C821789b99f9168330b06379c53813800',
        'cebsp_': '6',
        '_ce.s': 'v~03be6e16ef046c6d022e15b92f17fc805d3e5353~lcw~1706444420233~lva~1705841852261~vpv~0~v11.cs~435987~v11.s~98cca1f0-bdd7-11ee-8088-237c6f3b9eb5~v11.sla~1706444420241~v11.send~1706444419856~lcw~1706444420241',
        'stocks_tab_pv_counter': '2',
        '_ga_FFX3CZN1WY': 'GS1.1.1706444413.3.1.1706444420.0.0.0',
    }

    headers = {
        'authority': 'www.tipranks.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'GCLB=CJiS14vHsqS8cg; tr-experiments-version=1.14; tipranks-experiments=%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v4%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v4%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d; tipranks-experiments-slim=general_A%3av4%7cgeneral_B%3av4; rbzsessionid=497a17705398d1588cad843a0e929bc9; FPAU=1.2.874120930.1705841850; _fbp=fb.2.1705841849062.590562194; _fbp=fb.2.1705841849062.590562194; _gcl_au=1.1.1070310577.1705841851; _ce.irv=new; cebs=1; prism_90278194=3d912e60-8289-4304-945e-9376eb7e5e72; g_state={"i_l":0}; token=a0a1dcd179b1bb63bf838e7d15d510030604a18f; user=purushottamd.16@gmail.com,Purushottam Deshpande,; loginType=login; tr-plan-id=1; tr-plan-name=basic; tr-uid=7AE484BBD73059107360EB9C950B6753; rbzid=KnVq6vNn1X+rG2SNL8Y1ck+SYQZ+SBmQWgMDWt1konHREG7vij3hpp+woddQZQzBzvd93RFupauqYuJZJNnNPDdUPU4WRDwzeSTkIGD2iZzxHEwx5v4iWT1f4avgM0PW8qunxFcukhZmr2WdacVgo5snb5WoOmKiqWJW8n+KEVwiJgq1Qddmo6jLWIhZT2kF2R385cJLlxE0kGrKijYY5OdZA5GT3afFBYIcBo4h2zpo1GZSG9/ZGk7K48n/H7kqaOcRmw1GRvbjeug+neCz6gCEM88Cg167O8tTWoUm53Q=; TiPMix=68.69880258033942; x-ms-routing-name=self; IC_ViewCounter_www.tipranks.com=1; _ga=GA1.1.1570744259.1705841849; __gads=ID=04056718fbfc5622:T=1705841850:RT=1706444413:S=ALNI_MatpluSFD75Yiwo41vvfhpZ59Cmtw; __gpi=UID=00000cfbce05c9a0:T=1705841850:RT=1706444413:S=ALNI_MahPg_zSo-hlIvxEssMZ6ns2BqYbA; _ce.clock_event=1; _ce.clock_data=-21%2C2.51.77.139%2C1%2C821789b99f9168330b06379c53813800; cebsp_=6; _ce.s=v~03be6e16ef046c6d022e15b92f17fc805d3e5353~lcw~1706444420233~lva~1705841852261~vpv~0~v11.cs~435987~v11.s~98cca1f0-bdd7-11ee-8088-237c6f3b9eb5~v11.sla~1706444420241~v11.send~1706444419856~lcw~1706444420241; stocks_tab_pv_counter=2; _ga_FFX3CZN1WY=GS1.1.1706444413.3.1.1706444420.0.0.0',
        'referer': 'https://www.tipranks.com/stocks/ibkr/financials',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    params = {
        'tickers': symbol,
    }

    response = requests.get('https://www.tipranks.com/api/assets', params=params, cookies=cookies, headers=headers)

    return response.json()