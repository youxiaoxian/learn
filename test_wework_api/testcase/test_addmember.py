import allure
import pytest
from jsonpath import jsonpath
from test_wework_api.api.contact.member import Member

@allure.feature("通讯录成员管理")
class TestMember:
    def setup_class(self):
        self.member = Member()
        corpsecret = "zQtwpLtp5SWVvX4zLJvapfoTNeWIatsxbcxkkz1mzGw"
        self.member.get_token(corpsecret)

    @allure.title("成功读取成员")
    @pytest.mark.parametrize('userid',['DaXia'])
    def test_get_member(self,userid):
        r = self.member.get_member(userid)
        assert r.json()['errcode'] == 0
        assert r.json()['name'] == "测试"

    @allure.title("成功获取部门成员")
    @pytest.mark.parametrize('department_id,FETCH_CHILD',[[[1],1]])
    def test_get_department_member(self,department_id,FETCH_CHILD):
        r = self.member.get_department_member(department_id,FETCH_CHILD)
        assert r.json()['errcode'] == 0
        assert len(r.json()['userlist']) == 3


    @allure.title("成功创建成员")
    @pytest.mark.parametrize('userid,name,mobile,department',[['zhangsan','zhangsan','13800000000',[1]]])
    def test_add_member(self,userid,name,mobile,department):
        r = self.member.add_member(userid,name,mobile,department)

        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == "created"

        r = self.member.get_department_member(1, 0)
        assert userid in jsonpath(r.json(), '$..userid')

    @allure.title("创建成员")
    @pytest.mark.parametrize('userid,name,mobile,department',[['zhangsan1','zhangsan1','13900000000',[1,2]]])
    def test_add_member_mustache(self,userid,name,mobile,department):
        r = self.member.add_member_mustache(userid,name,mobile,department)
        assert r.json()['errcode'] == 0
        assert r.json()['errmsg'] == "created"





