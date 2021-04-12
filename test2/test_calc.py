from decimal import Decimal
import yaml

def get_param():
    with open("conf/param.yml") as f:
        param = yaml.safe_load(f)
    return param

class TestCal:

    def test_add_int(self,get_add_int_param_calc,inicalc_class):
        assert get_add_int_param_calc[2] == inicalc_class.add(get_add_int_param_calc[0], get_add_int_param_calc[1])


    def test_add_float(self, get_add_float_param_calc,inicalc_class):
        assert get_add_float_param_calc[2] == round(inicalc_class.add(get_add_float_param_calc[0], get_add_float_param_calc[1]),2)


    def test_div_int(self, get_div_int_param_calc,inicalc_class):
        try:
            assert Decimal(get_div_int_param_calc[2]).quantize(Decimal("0.00")) == Decimal(inicalc_class.div(get_div_int_param_calc[0], get_div_int_param_calc[1])).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')


    def test_div_float(self,get_div_float_param_calc,inicalc_class):
        try:
            assert Decimal(get_div_float_param_calc[2]).quantize(Decimal("0.00")) == Decimal(inicalc_class.div(get_div_float_param_calc[0], get_div_float_param_calc[1])).quantize(Decimal("0.00"))
        except ZeroDivisionError:
            print('ZeroDivisionError')
