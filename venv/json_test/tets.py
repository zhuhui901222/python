#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json


#json.dumps 用于将 Python 对象编码成 JSON 字符串。


data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json


#print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))


#json.loads
#json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text1 = json.loads(jsonData)
print text1
