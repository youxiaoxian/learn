import json

from jsonpath import jsonpath


class Test3:
    def test_3(self):
        # data = {
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     'method': 'get',
        #     "params": {
        #         "corpid": "wwd6da61649bd66fea",
        #         "corpsecret": "heLiPlmyblHRiKAgGWZky7MMvyld3d3QMUl5ra7NBZU"
        #     }
        # }
        #
        # if 'url' in data:
        #     print("data字典含url字段")
        # print(data.get("method"))
        # print(data['method'])
        with open('test3.json', encoding="UTF-8") as f:
            r = json.load(f)
        print(json.dumps(r, indent=2, ensure_ascii=False))
        tag_id_list1 = jsonpath(r, '$..tag[*].id')
        tag_id_list2 = [tag['id'] for group in r['tag_group'] for tag in group['tag']]
        # for group in r['tag_group']:
        #     for tag in group['tag']:
        #         print(tag['id'])
        print(tag_id_list1,tag_id_list2)

    # 根据tag_name_list获取tag_id
    def test_get_tag_id(self):
        tag_name_list= ['NAME1', 'NAME2']
        tag_id_list=[]
        with open('test3.json', encoding="UTF-8") as f:
            r = json.load(f)
        # tags 二维数组
        tags = jsonpath(r, '$..tag')
        print(tags[0][0])
        for k in range(len(tag_name_list)):
            for i in range(0, len(tags)):
                for j in range(0, len(tags[i])):
                    if tag_name_list[k] == tags[i][j]['name']:
                        tag_id_list.append(tags[i][j]['id'])
        print(tag_id_list)

    def test_get_tag_id(self):
        tag_name_list= ['NAME1', 'NAME2']
        tag_id_list=[]
        with open('test3.json', encoding="UTF-8") as f:
            r = json.load(f)
        assert 'NAME1'  in jsonpath(r,'$..*')
        print(jsonpath(r,'$..*'))


    # 根据tag_name_list获取tag_id_list，通过jsonpath
    def test_get_tag_id_list_2(self):
        with open('test3.json', encoding="UTF-8") as f:
            r = json.load(f)
        tag_name_list = jsonpath(r, '$..tag[*].name')
        print(tag_name_list)
        tag_id_list=[]
        print(tag_name_list)
        for tag_name in tag_name_list:
            # jsonpath返回结果为列表，[0]取出列表中的字符串
            tag_id_list.append(jsonpath(r,f"$..tag[?(@.name=='{tag_name}')].id")[0])
        print(tag_id_list)


        # jsonpath https://blog.csdn.net/lwg_1540652358/article/details/84111339
        # [?(< expression >)] 过滤表达式。 表达式必须求值为一个布尔值。
        # .< name > 点，表示子节点
        # jsonpath返回结果为列表，[0]取出列表中的字符串
        # print(jsonpath(r, f"$..tag[?(@.name=='NAME1')].id")[0])


