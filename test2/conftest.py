import pytest
import yaml

from test2.Calculator import Calculator

def get_param():
    with open("conf/param.yml",encoding='utf-8') as f: #mac默认是utf-8，而win默认是gbk，所有win执行需加encoding='utf-8'
        param = yaml.safe_load(f) #safe_load 将utf-8转换为unicode，用hook函数把unicode编码成utf8然后再解码成中文编码
    return param

#fixture实现set up和tear down
@pytest.fixture(scope='class')
def inicalc_class():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")

#fixture实现参数化
@pytest.fixture(params=get_param()['add_int'], ids=get_param()['ids'])
def get_add_int_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['add_float'], ids=get_param()['ids'])
def get_add_float_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['div_int'], ids=get_param()['ids'])
def get_div_int_param_calc(request):
    return request.param


@pytest.fixture(params=get_param()['div_float'], ids=get_param()['ids'])
def get_div_float_param_calc(request):
    return request.param

#hook函数
def pytest_collection_modifyitems(session, config, items: list):
    print("这是收集所有测试用例的方法")
    print(items)
    items.reverse()
    #用hook函数把unicode编码成utf8然后再解码成中文编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        print(item.name)
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
        print(item._nodeid)
