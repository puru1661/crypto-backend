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