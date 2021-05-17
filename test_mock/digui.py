import json
def recursion(base_data, int_data =1):
    """
    :param base_data: 原始的数据
    :return: 在原始数据基础之上，修改float 类型，对float 类型做数据翻倍操作
    """
    #
    if isinstance(base_data, dict):
        # 如果是字典类型，继续递归value值
        for k, v in base_data.items():
            base_data[k] = recursion(v,int_data)
    elif isinstance(base_data, list):
        # 递归算法，如果是list就继续遍历列表中的元素
        for i in base_data:
            recursion(i,int_data)
       # [recursion(i, int_data) for i in base_data]
    elif isinstance(base_data, float):
        # 对浮点型做倍增
        base_data = base_data * int_data
    else:
        base_data = base_data

    return base_data

if __name__ == '__main__':
    test_data = json.load(open("quote1.json", encoding="utf-8"))
    print(json.dumps(recursion(test_data, 2), indent=2))



