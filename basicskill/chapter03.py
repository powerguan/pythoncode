"""
函数:
圆柱体的体积公式 = PI * r*r * h
"""
import json

print(f"********简单粗暴的计算************")
# 求一个半径为2.5cm, 高为5cm的圆柱体体积
v1 = 3.14 * 2.5 * 2.5 * 5
print(f"v1 = {v1}")

# 求一个半径为35cm, 高为78cm的圆柱体体积
v2 = 3.14 * 35 * 35 * 78
print(f"v2 = {v2}")

# 求一个半径为24.3cm, 高为93.2cm的圆柱体体积
v3 = 3.14 * 24.3 * 24.3 * 93.2
print(f"v3 = {v3}")

print(f"\n********函数方式计算************")
"""
用函数来解决重复劳动, 必须先定义再使用 以下是函数定义
def 函数名(参数列表):
    函数体
    return 返回值

函数参数列表可以是0～N个, 返回值可以有也可以没有。  
"""


def calculateCylinderVolume(r : float, h: float) -> float :
    """
    该函数用于计算圆柱体体积，函数定义时参数叫形式参数简称形参
    :param r: 圆柱体地面半径
    :param h: 圆柱体高度
    :return: 圆柱体体积
    """
    PI = 3.14
    return PI * (r ** 2) * h


# 函数调用.程序是顺序执行的，但这里是先执行到36行，然后再执行25行但函数.
# 传入参数r=2.5, h=5, 2.5和5成为实参(实际参数)
v = calculateCylinderVolume(2.5, 5)
print(f"v1 = {v}")
print(f"v2 = {calculateCylinderVolume(h=78, r=35)}")
print(f"v3 = {calculateCylinderVolume(24.3, 93.2)}")


RedCodeDays = 7
YellowCodeDays = 3
GreenCodeDays = 0


def verifyNucleicAcid(days):
    if days > RedCodeDays:
        print(f"红码, 核酸{days}, 立即隔离")
    elif days > YellowCodeDays:
        print(f"黄码, 核酸{days}, 拒绝进入")
    else:
        print(f"绿码, 核算{days}, 欢迎光临")


verifyNucleicAcid(2)
verifyNucleicAcid(4)
# 没有return的函数返回值是None
print(f"test no return function: {verifyNucleicAcid(8)}")


# 参数默认值 和 返回多个值的函数
def checkNucleicAcid(days=3):
    if days > RedCodeDays:
        return "红码", "立即隔离"
    elif days > YellowCodeDays:
        return "黄码", "拒绝进入"
    else:
        return "绿码", "欢迎光临"


print(f"call func with default parameter: {checkNucleicAcid()}")
result = checkNucleicAcid(2)
print(f"{result[0]}, {result[1]}")
status, nextAction = checkNucleicAcid(9)
print(f"status={status}, next action: {nextAction}")


"""
斐波那契数列
学家莱昂纳多·斐波那契（Leonardo Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，斐波那契数列以如下被以递推的方法定义
F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
给定一个整数N，得到斐波那契数值
"""
callCounter = 0


def fibonacci(n):
    global callCounter
    callCounter += 1
    print(f"call counter: {callCounter}, n = {n}")
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# import time 模块
import time

begTime = time.time()
fibNum = 10
print(f"fibonacci({fibNum}) = {fibonacci(fibNum)}")
endTime = time.time()
print(f"calc {fibNum}, time cost: {endTime - begTime}")

# 用一个字典保存计算过的值
fibonacciDict = dict({})


def fibonacci2(n):
    global fibonacciDict
    if n == 0 or n == 1:
        return 1
    else:
        if not (n in fibonacciDict):  # 等同于 (n in fibonacciDict) == False
            fibonacciDict[n] = fibonacci2(n - 1) + fibonacci2(n - 2)

        return fibonacciDict[n]


begTime = time.time()
fibNum = 200  # 毕竟是递归函数，不支持过深的递归调用
print(f"fibonacci({fibNum}) = {fibonacci2(fibNum)}")
endTime = time.time()
print(f"calc {fibNum}, time cost: {endTime - begTime}")

# 非递归版本的斐波那契数列
fibonacciDict = dict({})


def fibonacci3(n):
    global fibonacciDict
    n1 = 1
    n2 = 1
    if (n <= 2):
        return 1
    else:
        if (n in fibonacciDict):
            return fibonacciDict[n]
        else:
            i = 2
            n3 = 0
            while (i < n):
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                i += 1
                fibonacciDict[i] = n3

            return n3


begTime = time.time()
fibNum = 20000
print(f"fibonacci({fibNum}) = {fibonacci3(fibNum)}")
endTime = time.time()
print(f"calc {fibNum}, time cost: {endTime - begTime}")

fibNum = 2000
print(f"fibonacci({fibNum}) = {fibonacci3(fibNum)}")
endTime = time.time()
print(f"calc {fibNum}, time cost: {endTime - begTime}")

fibNum = 1000
print(f"fibonacci({fibNum}) = {fibonacci3(fibNum)}")
endTime = time.time()
print(f"calc {fibNum}, time cost: {endTime - begTime}")

"""
总结:
1. 函数的好处是减少重复代码，代码复用和提高开发效率;
2. 调用函数时不指定参数名字，传入的实参顺序就是形参顺序;指定了名字顺序可以任意交换.
3. 函数可以嵌套调用;
4. 队列是先进先出;
5. 栈是先进后出;
"""

"""
文件读写三种模式:
r: 读模式
w: 清空并写模式，如果文件已经存在会清空文件内容；如果文件不存在会创建新文件
a: 追加写模式,如果文件存在会在文件后面追加内容，如果文件不存在会创建文件
"""
#清空写文件
#step1 打开
file = open("./test.json", 'w', encoding="UTF-8")
#step2: 写文件
mixDict = dict({
    "北京": 19,
    "天津": 25,
    "oakville": 15,
    '成都': 30
})
import json
jsonStr = json.dumps(mixDict) #json.dumps(mixDict, ensure_ascii=False)
file.write(jsonStr)
#file.flush()
#file.write(jsonStr)
#step3 关闭
file.close()

#追加写文件
#step1 打开
file = open("./test.json", 'a', encoding="UTF-8")
#step2: 写文件
mixDict = dict({
    "海淀": 33,
    "朝阳": 32,
    "西城": 30
})
jsonStr = json.dumps(mixDict) #json.dumps(mixDict, ensure_ascii=False)
file.write(jsonStr)

#写文件时先缓存到内存，缓冲区快满了的时候才会往磁盘写入,如果想提前往磁盘写入可以用flush函数写入磁盘
#file.flush()
#file.write(jsonStr)
#step3 关闭
file.close()

#读文件
#step1: open file
file = open("./test.json", 'r', encoding="UTF-8")
#step2: read file
partialContent = file.read(10)
print(f"partial content is: {partialContent}", end="\n\n")
allContent = file.read()
print(f"all content is: {allContent}", end="\n\n")
#read by lines
file.seek(0) #将读取指针移动到文件开头
for line in file.readlines():
    print(f"line = {line}")

file.seek(0)
print(f"readline() result = {file.readline()}")
print(f"readline() result = {file.readline()}")
print(f"readline() result = {file.readline()}")

#step3: clos file
file.close()

"""
打开不存在的文件与异常捕获
try - except
"""
try:
    file = open("./test1.json", 'r', encoding="UTF-8")
    allContent = file.read()
    print(f"all content is: {allContent}", end="\n\n")
    file.close()
except FileNotFoundError as ex:
    print(f"have a error {ex}")
