import time
import yaml
from selenium import webdriver

class TestWework:
    def test_wework(self):
        # 复用只支持chrome浏览器
        options=webdriver.ChromeOptions()
        # 设置debug地址
        options.debugger_address='127.0.0.1:9222'
        driver=webdriver.Chrome(options=options)
        # driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        driver.implicitly_wait(5)
        # time.sleep(5)
        # print(driver.page_source)
        # driver.find_element_by_id("menu_contacts").click()
        # 在当前页面点击通讯录
        driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        time.sleep(5)
        #在通讯录页面点击添加成员
        driver.find_element_by_xpath('//*[@id="js_contacts41"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        # 获取cookie信息
        cookie = driver.get_cookies()
        # 把cookie存如yaml文件内
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


