#!usr/bin/env python
# -*- coding:utf-8 -*-
# 如果获取的数据不是直接可以展示的结构
# 方式一
user_list = [
    {"id":222,"name":"haiyan","age":33},
    {"id":2,"name":"zzzzz","age":13}
]
new_user_list = []
for item in user_list:
    item["age"] = item["id"]+item["age"]
    new_user_list.append(item["age"])
# print(new_user_list)
# print(user_list)

# 方式二:利用迭代器
def test():
    user_list = [
        {"id":222,"name":"haiyan","age":33},
        {"id":2,"name":"zzz","age":13}
    ]
    for item in user_list:
        yield {"id":item["id"],"name":item["name"],"age":item["id"]+item["age"]}
obj = test()
# print(obj.__next__())
# print(next(obj))

# 方式三：利用类、__iter__、yield实现
class Foo(object):
    def __init__(self,arg):
        self.arg = arg
    def __iter__(self):
        for item in self.arg:
            yield item
            yield {"age":item["age"]+item["id"]}
def test():
    user_list = [
        {"id": 222, "name": "haiyan", "age": 33},
        {"id": 2, "name": "zzz", "age": 13}
    ]
    obj = Foo(user_list)   #一实例化类就会去调用__init__方法
    for i in obj:
        print(i)
test()

l = [1,2]
print(len(l))

