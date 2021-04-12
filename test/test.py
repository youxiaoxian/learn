import yaml

def get_param():
    param=yaml.safe_load(open("param.yml"))
    return param

print(get_param())
print(get_param()['add_int'])
print(get_param()['add_float'])
print(get_param()['div_int'])
print(get_param()['div_float'])
print(get_param()['ids'])