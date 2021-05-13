import json
import jsonpath
with open('response.json', encoding="UTF-8") as f:
    load_dict=json.load(f)

load_data=json.dumps(load_dict)
print(load_dict)
print(type(load_dict))
print(load_data)
print(type(load_data))

print(load_dict['data'][0]['config']['value'][0]['name'])
print(jsonpath.jsonpath(load_dict, '$.data[0].config.value[0].name'))