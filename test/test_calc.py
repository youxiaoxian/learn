from decimal import Decimal
import pytest
import yaml
from test.Calculator import Calculator

def get_param():
    param = yaml.safe_load(open("param.yml"))
    return param


class TestCal:
    def setup_class(self):
        print("所有计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("所有计算结束")

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', get_param()['add_int'], ids=get_param()['ids'])
    def test_add_int(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', get_param()['add_float'], ids=get_param()['ids'])
    def test_add_float(self, a, b, expect):
        assert expect == round(self.calc.add(a, b),2)

    @pytest.mark.parametrize('a,b,expect', get_param()['div_int'], ids=get_param()['ids'])
    def test_div_int(self, a, b, expect):
        try:
            assert Decimal(expect).quantize(Decimal("0.00")) == Decimal(self.calc.div(a, b)).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')

    @pytest.mark.parametrize('a,b,expect', get_param()['div_float'], ids=get_param()['ids'])
    def test_div_float(self, a, b, expect):
        try:
            assert Decimal(expect).quantize(Decimal("0.00")) == Decimal(self.calc.div(a, b)).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')
