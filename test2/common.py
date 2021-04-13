import yaml
def get_param():
    with open("conf/param.yml",encoding='utf-8') as f: #mac默认是utf-8，而win默认是gbk，所有win执行需加encoding='utf-8'
        param = yaml.safe_load(f) #safe_load 将utf-8转换为unicode，用hook函数把unicode编码成utf8然后再解码成中文编码
    return param