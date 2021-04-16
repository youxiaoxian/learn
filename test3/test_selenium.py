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

    def test_driver(self):
        self.driver.get("http://192.168.7.147:3000/")
        self.driver.find_element_by_xpath('//*[@id="login-view"]/form/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="inputPassword"]').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="login-view"]/form/div[3]/button').click()
        time.sleep(3)
        # 获取cookie信息
        cookie=self.driver.get_cookies()
        print(cookie)
        # 把cookie存如yaml文件内
        with open('cookie.yml','w',encoding='utf-8') as f:
            yaml.dump(cookie,f)
    def test_cookie(self):
        self.driver.get("http://192.168.7.147:3000/")
        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_cookie = yaml.safe_load(f)
            print(yaml_cookie)
            for cookie in yaml_cookie:
                self.driver.add_cookie(cookie)
            print(cookie)
        time.sleep(5)
        self.driver.get("http://192.168.7.147:3000/d/9CWBz0bik/xi-tong-jian-kong-mian-ban?orgId=1&refresh=10s&var-job=node&var-hostname=All&var-node=192.168.7.147:9100&var-maxmount=%2Fdata&var-env=&var-name=&from=now-5m&to=now")
        time.sleep(5)








