import time
import yaml
from selenium import webdriver

class TestWework:
    def test_wework(self):
        options=webdriver.ChromeOptions()
        options.debugger_address='127.0.0.1:9222'
        driver=webdriver.Chrome(options=options)
        # driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        driver.implicitly_wait(5)
        # time.sleep(5)
        # print(driver.page_source)
        # driver.find_element_by_id("menu_contacts").click()
        driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        cookie = driver.get_cookies()
        with open("data.yaml","w",encoding="UTF-8") as f:
             yaml.dump(cookie,f)

def test_cookie():
    # 实例化 driver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        print(yaml_data)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(5)


