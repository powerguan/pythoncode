"""
本文件包含以下内容.
1. 变量;
2. 数字;
3. 字符串;
4. 运算符;
5. 位运算符;
"""

"""
1. 变量与类型
python是无类型语言，意思是定义变量时不需要指定类型，python解释器能自动推导变量的类型.
2杯12.8的拿铁咖啡
"""

coffeeType = "拿铁"  # 赋值语句 也可以叫做 一个表达式, 等号左边是变量，等号右边是值
coffeePrice = 12.8
coffeeCount = 2

"""
coffeeType， coffeePrice, coffeeCount 三个是变量的数据类型分别是 字符串(string), 浮点(float), 整数(integer/int)
变量的数据类型由python自己推导出来的. 
用type()函数测试一个变量的类型，这个函数返回一个描述被测试对象类型的字符串.
"""
print(f"coffeeType is:  {type(coffeeType)}")
print(f"coffeePrice is: {type(coffeePrice)}")
print(f"coffeeCount is: {type(coffeeCount)}")

# 变量的数据类型是可以改变的
coffeeType = 2
coffeePrice = "拿铁"
coffeeCount = 12.8
print(f"coffeeType is:  {type(coffeeType)}")
print(f"coffeePrice is: {type(coffeePrice)}")
print(f"coffeeCount is: {type(coffeeCount)}")

"""
[总结]
1. 定义变量的命名规范是，以小写字母开头的名词, 由字母，数字和下划线组成;
2. 函数是以小写字母开头的动词, 由字母，数字和下划线组成;
3. 变量的类型是由python根据code上下文自动推导，程序员心里是要知道变量在某个位置是什么类型的数据;
4. python的简单数据类型有三种: string, float, int;
"""

"""
2. 数字类型
a. Int， b. Float
支持 加减乘除运算
"""
sumValue = 10 + 50
subValue = 10 - 3
mulValue = 10 * 2
divValue = 10 / 2
roundValue = 10 // 3
modValue = 10 % 3
expValue = 10 ** 3
print(f"sumValue = {sumValue}")
print(f"subValue = {subValue}")
print(f"mulValue = {mulValue}")
print(f"divValue = {divValue}")
print(f"roundValue = {roundValue}")
print(f"modValue = {modValue}")
print(f"expValue = {expValue}")
print("*****end of first calculate******")

sumValue += 5  # sumValue = sumValue + 5
subValue -= 2  # sumValue = sumValue - 2
mulValue *= 2  # sumValue = sumValue * 2
divValue /= 2  # sumValue = sumValue / 2
roundValue //= 2  # sumValue = sumValue // 2
modValue %= 2  # sumValue = sumValue % 2
expValue **= 2  # sumValue = sumValue ** 2
print(f"sumValue = {sumValue}")
print(f"subValue = {subValue}")
print(f"mulValue = {mulValue}")
print(f"divValue = {divValue}")
print(f"roundValue = {roundValue}")
print(f"modValue = {modValue}")
print(f"expValue = {expValue}")
print("*****end of second calculate******")

"""
[隐式类型转换]
在计算机里float占的字节数比int多，也就是float比int可以存储更大的数。所有的编程语言在处理数字运算时都会将占位少的数字类型转化为占位大的。
3+2=5 : 因为3和2都是int，所以相加时都以int类型做运算,其结果也是int;
3+2.0=5.0 : 因为3是int，2.0是float，在运算之前需要把3转化为float（3.0），然后在做加法运算，得到的结果也是float。计算机不会像人一样发现结果是int就记为整数，只会严格遵守计算前的数据类型.
"""
sum1 = 3 + 2
print(f"sum type: {type(sum1)}")  # 类型为int
sum2 = 3 + 2.0
print(f"sum type: {type(sum2)}")  # 类型为float

"""
字符串
一段文本就是字符串，字符串不支持算术运算符.
"""
strValue = "我是字符串, you can print out me in console !!!"
print(strValue)

strValue = "我是字符串, please call me \"String' "
print(strValue)

strValue = '我是字符串, please call me \"String\''
print(strValue)

# 两个字符串可以用 + 进行拼接，而不是加法.
strValue = "我是字符串"
strValue += ", 你猜为什么我也支持加法操作符?"  # strValue = strValue + ", 你猜为什么我也支持加法操作符?"
print(strValue)

# 字符串常用函数
# join: 将字符串数组的所有成员拼接
strValue = ".".join(["I am programmer", "join", "my name is Jason"])
print(strValue)
# split: 将字符串按照某个字符切分成数组
items = strValue.split(" ")
print(items)
# len: 取字符串长度
print("strValue = {len(strValue)}")
print(f"strValue = {len(strValue)}") #字符串 插值法
# [start:end:stop]： 取子串操作
strValue = "1234567890"
print(f"{strValue[0:5:1]}")
print(f"{strValue[0:5:2]}")
print(f"{strValue[::-1]}")
# startWith: 判断字符串是否以某个字串开头
print(f"start with '123': {strValue.startswith('123')}")
print(f"end with '890': {strValue.endswith('890')}")

"""
字符串与数字间互相转换
"""
# 字符串转整数 int()
strValue = "110"
numValue = int(strValue)
print(f"{numValue} * 2 = {numValue * 2}")

# 整数转字符串 str()
numValue = 120
strValue = str(numValue)
print(f"strValue type is: {type(strValue)}")


print(f"have a good day")