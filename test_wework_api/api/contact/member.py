import allure
import pystache
import yaml

from test_wework_api.api.wework_api import WeWork

class Member(WeWork):

    @allure.step("读取成员")
    def get_member(self,userid):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get?",
            "method": "GET",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("创建成员")
    def add_member(self,userid,name,mobile,department):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create?",
            "method": "POST",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("获取部门成员")
    def get_department_member(self,department_id,FETCH_CHILD):
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?",
            "method": "GET",
            "params": {
                "access_token": self.token,
                "department_id": department_id,
                "fetch_child": FETCH_CHILD

            }
        }
        r = self.http_request(data)
        self.save(data, r)
        return r

    @allure.step("创建成员,mustache方法")
    def add_member_mustache(self,userid,name,mobile,department):
        with open("../data/create_data.yaml", encoding="UTF-8") as f:
            body = yaml.safe_load(f)
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create?",
            "method": "POST",
            "params": {
                "access_token": self.token
            },
            "json": body
        }
        template=  {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }

        body["userid"] = pystache.render(body["userid"], template)
        body["name"] = pystache.render(body["name"], template)
        body["mobile"] = pystache.render(body["mobile"], template)
        r = self.http_request(data)
        self.save(data, r)
        return r