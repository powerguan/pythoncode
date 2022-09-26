
"""
本文件讲解变量,简单数据类型.
[简单数据类型]
python是无类型语言，意思是定义变量时不需要指定类型，python解释器能自动推导变量的类型.
[例子]
"""

# 2杯12.8的拿铁咖啡
coffeeType = "拿铁"  #赋值语句 也可以叫做 一个表达式, 等号左边是变量，等号右边是值
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
1. 定义变量的命名规范是，以小写字母开头的名词;
2. 函数是以小写字母开头的动词;
3. 变量的类型是由python根据code上下文自动推导，程序员心里是要知道变量在某个位置是什么类型的数据;
4. python的简单数据类型有三种: string, float, int;
"""