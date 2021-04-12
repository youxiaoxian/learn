import pytest

from test2.Calculator import Calculator
from test2.test_calc import get_param

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
