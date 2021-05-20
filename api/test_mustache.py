import json
import pystache
import requests
import yaml

class TestAPI:
    def test_api(self):
        data = {
            "appid": "{{appid}}",
            "startTime": "2021-05-05 00:00:00",
            "endTime": "2021-05-12 14:59:59",
            "curpage": "{{curpage}}",
            "pagesize": "50"
        }
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_datas = yaml.safe_load(f)
            print(yaml_datas)
        # template = {'appid':'test002','curpage': '1'}
        for yaml_data in yaml_datas:
            data["appid"] = pystache.render(data["appid"],yaml_data)
            data["curpage"] = pystache.render(data["curpage"],yaml_data)
            print(data)
            r = requests.post('http://192.168.7.147:22010/dataanalysis/gwsummaryanalysis',json=data)
            print(r.status_code)
            print(json.dumps(r.json(),indent=2,ensure_ascii=False))