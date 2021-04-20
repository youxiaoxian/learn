import yaml
from selenium import webdriver


class Base:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("../conf/data.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            print(yaml_data)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(3)
