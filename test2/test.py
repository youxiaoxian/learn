import pytest
import yaml


def get_param():
    with open("conf/param.yml") as f:
        param = yaml.safe_load(f)
    return param

print(get_param())

@pytest.fixture(params=get_param()['add_int'], ids=get_param()['ids'])
def get_add_int_param_calc(request):
    return request.param

def test_a(get_add_int_param_calc):
    print(get_add_int_param_calc)
    print(get_add_int_param_calc[1])
