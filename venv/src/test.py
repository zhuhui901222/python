#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)

print "Hello, World!";

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    # 没有严格缩进，在执行时会报错
    print "False"

item_one=1
item_two=2
item_three=3
total = item_one + \
        item_two + \
        item_three

print total


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']


word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

print paragraph


#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# 第一个注释
print "Hello, Python!";  # 第二个注释

name = "Madisetti" # 这是一个注释



'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#raw_input("按下 enter 键退出，其他任意键显示...\n")

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y

"""
if expression :
   suite
elif expression :
   suite
else :
   suite
"""

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name

str = 'Hello World!'

print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串


#列表

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表


#元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组


tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用



#字典

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值


#运算符

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print "6 - c 的值为：", c

a = 10
b = 5
c = a//b
print "7 - c 的值为：", c


print  1/2
print  1/float(2)


a = 21
b = 10
c = 0

if ( a == b ):
   print "1 - a 等于 b"
else:
   print "1 - a 不等于 b"

if ( a != b ):
   print "2 - a 不等于 b"
else:
   print "2 - a 等于 b"

if ( a <> b ):
   print "3 - a 不等于 b"
else:
   print "3 - a 等于 b"

if ( a < b ):
   print "4 - a 小于 b"
else:
   print "4 - a 大于等于 b"

if ( a > b ):
   print "5 - a 大于 b"
else:
   print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
   print "6 - a 小于等于 b"
else:
   print "6 - a 大于  b"

if ( b >= a ):
   print "7 - b 大于等于 a"
else:
   print "7 - b 小于 a"


a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;        # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;        # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;           # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;       # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;       # 15 = 0000 1111
print "6 - c 的值为：", c

a = 10
b = 20

if ( a and b ):
   print "1 - 变量 a 和 b 都为 true"
else:
   print "1 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
   print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if ( a and b ):
   print "3 - 变量 a 和 b 都为 true"
else:
   print "3 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
   print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "4 - 变量 a 和 b 都不为 true"

if not( a and b ):
   print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
   print "5 - 变量 a 和 b 都为 true"

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"

if ( b not in list ):
   print "2 - 变量 b 不在给定的列表中 list 中"
else:
   print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if ( a in list ):
   print "3 - 变量 a 在给定的列表中 list 中"
else:
   print "3 - 变量 a 不在给定的列表中 list 中"

#身份运算符用于比较两个对象的存储单元


a = 20
b = 20

if ( a is b ):
   print "1 - a 和 b 有相同的标识"
else:
   print "1 - a 和 b 没有相同的标识"

if ( a is not b ):
   print "2 - a 和 b 没有相同的标识"
else:
   print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if ( a is b ):
   print "3 - a 和 b 有相同的标识"
else:
   print "3 - a 和 b 没有相同的标识"

if ( a is not b ):
   print "4 - a 和 b 没有相同的标识"
else:
   print "4 - a 和 b 有相同的标识"



flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name              # 条件不成立时输出变量名称




num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine


var = 100

if ( var  == 100 ) : print "变量 var 的值为100"

print "Good bye!"



# 循环

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"



i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

"""
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"

"""


count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"



for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit

print "Good bye!"


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

print "Good bye!"



for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'





for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print '当前字母 :', letter

var = 10                    # 第二个实例
while var > 0:
   print '当前变量值 :', var
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break

print "Good bye!"


for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print '当前字母 :', letter

var = 10                    # 第二个实例
while var > 0:
   var = var -1
   if var == 5:
      continue
   print '当前变量值 :', var
print "Good bye!"



# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"


import random

print random.uniform(1,100)



var1 = 'Hello World!'
var2 = "Python Runoob"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]


var1 = 'Hello World!'

print "更新字符串 :- ", var1[:6] + 'Runoob!'


##
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if( "H" in a) :
    print "H 在变量 a 中"
else :
    print "H 不在变量 a 中"

if( "M" not in a) :
    print "M 不在变量 a 中"
else :
    print "M 在变量 a 中"

print r'\n'
print R'\n'


print "My name is %s and weight is %d kg!" % ('Zara', 21)


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]


list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print list


list1 = ['physics', 'chemistry', 1997, 2000]

print list1
del list1[2]
print "After deleting value at index 2 : "
print list1
print len(list1)



#元组
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]


tup = ('physics', 'chemistry', 1997, 2000);

print tup;
del tup;
print "After deleting tup : "
#print tup;


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry


print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
#del dict ;        # 删除词典



##键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行


import time;  # 引入time模块



ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;


# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");



# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return

# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist



#不定长参数   可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;

# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )


# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print "函数内 : ", total
   return total;

# 调用sum函数
total = sum( 10, 20 );

print total


#模块

#Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：

from math import *


#dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。

import math

content = dir(math)

print content;

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1

print Money
AddMoney()
print Money


from runoob1 import runoob1
from runoob2 import runoob2

runoob1()
runoob2()



#str = raw_input("请输入：")
#print "你输入的内容是: ", str


#str = input("请输入：")
#print "你输入的内容是: ", str
#输入  [x*5 for x in range(2,10,2)]



# 打开一个文件
fo = open("foo.txt", "a")
fo.write( "www.runoob.com!\nVery good site!\n")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
fo.close()



# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()

import os

# 重命名文件test1.txt到test2.txt。
#os.rename( "test1.txt", "test2.txt" )
#删除
#os.remove("test2.txt")
#创建目录
#os.mkdir("newdir")


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()


#try-finally 语句无论是否发生异常都将执行最后的代码。

try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz");

def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
# 打包为元组的列表
print zipped
# 元素个数与最短的列表一致
print zip(a,c)
# 与 zip 相反，可理解为解压，返回二维矩阵式
print zip(*zipped)


l = ['a', 'b', 'c', 'd', 'e','f']
print l

#打印列表
print zip(l[:-1],l[1:])


###内置函数

#绝对值
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)


#python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

print divmod(7, 2)

print divmod(8, 2)

print divmod(1+2j,1+0.5j)


#静态方法
#python staticmethod 返回函数的静态方法。
#该方法不强制要求传递参数，如下声明一个静态方法：


class C(object):
    @staticmethod
    def f():
        print('runoob');

C.f();          # 静态方法无需实例化
cobj = C()
cobj.f()        # 也可以实例化后调用

#all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。
print   all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0

print   all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素

print   all([0, 1,2, 3])          # 列表list，存在一个为0的元素

print   all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0

print   all((0, 1,2, 3))          # 元组tuple，存在一个为0的元素

print    all([])             # 空列表

print   all(())             # 空元组


#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
seasons =['Spring', 'Summer', 'Fall', 'Winter']
#a=list(enumerate(seasons))

#b=list(enumerate(seasons, start=1))       # 小标从 1 开始


i = 0
seq = ['one', 'two', 'three']
for element in seq:
    print i, seq[i]
    i +=1

for i, element in enumerate(seq):
    print i, seq[i]


#int() 函数用于将一个字符串或数字转换为整型。
print int(3)

print int(3.6)

print  int('12',16)

print int('0xa',16)

print int('10',8)


#ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
print ord('a')

print  ord('b')

print  ord('c')


#str() 函数将对象转化为适于人阅读的形式。


s = 'Hello, world.'
#str(s)
print  repr(s)

#any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。

print any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0

print  any(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素

print   any([0, '', False])        # 列表list,元素全为0,'',false

print   any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0

print   any(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素

print   any((0, '', False))        # 元组tuple，元素全为0,'',false

print   any([]) # 空列表   #false

print    any(()) # 空元组  #false


#eval() 函数用来执行一个字符串表达式，并返回表达式的值。
x = 7
print  eval( '3 * x' )

print   eval('2 + 2')

print   eval('pow(2,2)')

n=81
print   eval("n + 4")


#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
#isinstance() 会认为子类是一种父类类型，考虑继承关系。
a = 2
print  isinstance (a,int)
#print  isinstance (a,(str,int,list))    # 是元组中的一个返回 True
# isinstance() arg 2 must be a class, type, or tuple of classes and types

#basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。

#print  isinstance("Hello world", str)

print  isinstance("Hello world", basestring)

#execfile() 函数可以用来执行一个文件。
execfile('exec.py')







