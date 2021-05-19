import json

import requests
class TestAPI:
    def test_api(self):
        # r = requests.get('https://httpbin.testing-studio.com/get')
        data = {
            "appid": "test002",
            "startTime": "2021-05-05 00:00:00",
            "endTime": "2021-05-12 14:59:59",
            "curpage": "1",
            "pagesize": "50"
        }
        print(type(data))
        # headers = {
        #     'Content-Type': 'application/json'
        # }
        r = requests.post('http://192.168.7.147:22010/dataanalysis/gwsummaryanalysis',json=data)
        print(r.status_code)
        print(json.dumps(r.json(),indent=2,ensure_ascii=False))
        print(type(r.json()))
        print(r.text)
        print(type(r.text))