import time

import yaml
from selenium import webdriver

class TestDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_cookie(self):
        self.driver.get("http://192.168.7.147:22000/")
        _cookies = {
            'ab_sr': '1.0.0_MzcxMTJlNTFiYzE4ZmU0NDMwOGIxMTZjMzQxMzVhYmJjMmQ4Y2ExNTZkMjMxYzdjNTI0NjQ1YjkwNTc5ZDIzMTdjODE2ZmZiYWRiZGYxNTcyZWVlYzA0NDk0ZTdiNmQ4',
            'sidebarStatus': '0',
            'BAIDUID_BFESS': '1B77139D0F8498A770AD52B542337C20:FG=1',
            'Admin-Token': '%E7%99%BB%E5%BD%95%E6%88%90%E5%8A%9F',
            'shiro.session': '1fc735d2-d0fd-4b5e-be04-b026e367bf5d'
        }
        cookie_list = []
        for k, v in _cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
            cookie_list.append({"name": k, "value": v})
            # print(k,v)
        print(cookie_list)
        self.driver.get("http://192.168.7.147:22000/#/terminalMGT/terminalList")
        time.sleep(5)

    def test_cookie2(self):
        self.driver.get("http://192.168.7.147:22000/")
        with open("cookie2.yml", encoding="UTF-8") as f:
            _cookies = yaml.safe_load(f)
            print(_cookies)
            print(type(_cookies))
        for k, v in _cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("http://192.168.7.147:22000/#/terminalMGT/terminalList")
        time.sleep(5)









