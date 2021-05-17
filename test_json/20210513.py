import json
import jsonpath

# json.dump() 将dict数据转换为json数据后写入json文件
# json.load() 读取json文件数据，转成dict数据
with open('response.json', encoding="UTF-8") as f:
    load_dict=json.load(f)

print(load_dict)
print(type(load_dict))

# json.dumps()将Python dict数据结构转换为JSON （json是字符串）
# json.loads()将JSON编码字符串还原为Python dict数据结构
load_data=json.dumps(load_dict)
print(load_data)
print(type(load_data))

print(load_dict['data'][0]['config']['value'][0]['name'])
# print(jsonpath.jsonpath(load_dict, '$.data[0].config.value[0].name'))