"""
本章节讲解容器数据类型,包括List, Tuple, Set, Dict
"""

"""
List: 将多个元素放入中括号，且元素之间以逗号隔开. List又叫数组
"""
print("**************List**************")
numList = [1, 2, 3, 4, 5]
print(f"num list is: {numList}， and it's type is: {type(numList)}")
# 定义空列表可以用如下2种方法
numList = []
numList = list() #推荐这种
# 二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"matrix is: {matrix}, and it's type is: {type(matrix)}")
# 列表的访问方式 下标索引
mixList = ["Victor", 98, "Power", 99]
for i in range(0, len(mixList)):
    print(f"No.{i} = {mixList[i]}")

# 列表的常用函数
print(f"index(98) = {mixList.index(98)}")  # index: 返回成员在列表中的下标索引
mixList[1] = 99  # 通过下标索引方式直接修改某个位置元素的值
print(f"mixList = {mixList}, size = {len(mixList)}")
mixList.insert(2, "China")  # 在指定位置插入一个元素，该位置及其后面的元素自动往后移动
print(f"mixList = {mixList}, size = {len(mixList)}")
mixList.append("Nationality Day")  # 在列表的尾部追加一个元素
print(f"mixList = {mixList}, size = {len(mixList)}")
mixList.extend([100, "01/Oct", 100, "02/Oct", "03/Oct"])  # 在列表的尾部追加多个元素
print(f"mixList = {mixList}, size = {len(mixList)}")
del mixList[10]  # 删除指定位置的元素
print(f"mixList = {mixList}, size = {len(mixList)}")
popElement = mixList.pop(9)  # 取出指定位置的元素
print(f"pop element is {popElement}, after that mixList = {mixList}, size = {len(mixList)}")
mixList.remove(100)  # 查找并删除第一个出现的元素
print(f"after remove 100, mixList = ${mixList}, size = {len(mixList)}")
print(f"mixList has 99: {mixList.count(99)}")  # 统计列表中有多少个指定的元素
mixList.clear()  # 清空列表
print(f"mixList = {mixList}, size = {len(mixList)}")

# 遍历列表
# 构造一个list
for i in range(0, 10):
    mixList.append(i)
print(f"mixList is: {mixList}, mixList size: {len(mixList)}")
# 1. while
index = 0
while index < len(mixList):
    mixList[index] *= 2
    index += 1
print(f"mixList is: {mixList}, mixList size: {len(mixList)}")

# 2. for
for element in mixList:
    print(f"mixList element is: {element}")
"""
总结:
1. list里的元素的类型可以是任意类型，并不要求必须为同一种类型;
2. list可以嵌套, 也就是说元素也可以是另一个list.这样嵌套下去可以有三维，四维甚至n维的列表.
3. list的访问方式是用下标索引，从左到右索引值从0开始，从右到左是从-1，-2，-3，...
"""

"""
Tuple: 将元素放到圆括号里，元素间以逗号隔开。与List的区别是把中括号改为圆括号,另一个区别是不支持修改，一旦定义不能再改了.
"""
print("\n**************Tuple**************")
mixTuple = (1, 3, 5, "打老虎")
print(f"mixTuple is: {mixTuple}, type is: {type(mixTuple)}")
#定义空tuple
emptyTuple = tuple()
print(f"emptyTuple type is: {type(emptyTuple)}")
#定义一个元素的tuple
oneTuple = tuple("abc")
print(f"oneTuple type is: {type(oneTuple)}")



"""
控制语句:
if elseif
"""
print(f"打印99乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j}\t", end='')
    print()

"""
异常捕获
try - except
"""
try:
    print(f"I am try-catch")
    print(f"this value is: {10 / 0}")
except ZeroDivisionError as ex:
    print(f"have a error {ex}")
