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
tuple因为是只读(read only)的list, 所以常用的函数就三个 count, index, len 
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
#另一个定义元素的tuple
oneTuple = ("abc", )
print(f"oneTuple type is: {type(oneTuple)}")

"""
序列的切片操作: 从一个序列(list, tuple, string)中取出一个子序列,并返回，序列操作并不会改变序列原始值.
切片语法: list[start:end:step]
"""
print("\n**************Slice**************")
numList = [1, 2, 3, 4, 5]
#取出位置是奇数的子序列
subList = numList[0:len(numList):2]
print(f"sub list is: {subList}")
#step为负数表示从尾巴到头取，下面这行代码等同于颠倒序列 [5, 4, 3, 2, 1]
subList = numList[::-1]
print(f"sub list is: {subList}")

"""
Set: 集合，用大括号来定义集合，集合成员用逗号隔开. 
set是无序的，不能用下标索引访问元素
"""
print("\n**************Set**************")
#定义集合
mixSet = {1, 2, 3, "name", "price", 10.5, 3} #初始化时输入2个3,但最后只会保留1个3.
print(f"mixSet type: {type(mixSet)}, mixSet is: {mixSet}")
#常用函数
mixSet.add(4)           #添加新元素
print(f"after add mixSet is: {mixSet}")
mixSet.remove(1)        #删除某个元素,参数是元素而不是索引.
print(f"after remove mixSet is: {mixSet}")
popElement = mixSet.pop() #从集合随机取出一个元素
print(f"pop element is: {popElement}, after pop mixSet is: {mixSet}")
print(f"mixSet size: {len(mixSet)} ") #统计集合的size
mixSet.clear()          #清空集合
print(f"after remove mixSet is: {mixSet}")
#两个集合的运算, 结果是一个新集合
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}
#差集 set1 - set2: 从set1里把同时也存在于set2的元素删除，剩下的元素生成新集合
diffSet = set1.difference(set2)
print(f"set1 is: {set1}")   #set1不变
print(f"set2 is: {set2}")   #set2不变
print(f"diffSet is: {diffSet}") #diffSet is: {1, 2, 3, 4}
#消除差集
set1.difference_update(set2) #将set1中同时存在于set2的元素删除，结果是set1被改变，set2不变
print(f"set1 is: {set1}")   #set1里的5，6被删除
print(f"set2 is: {set2}")   #set2不变
#合并集合, 将两个集合的元素合并，并去除重复的元素后生成一个新元素，原集合不变
print(f"\nset union")
set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10}
unionSet = set1.union(set2)
print(f"set1 is: {set1}")   #set1不变
print(f"set2 is: {set2}")   #set2不变
print(f"unionSet is: {unionSet}")

print(f"\nset intersection")
interSet = set1.intersection(set2)
print(f"set1 is: {set1}")   #set1不变
print(f"set2 is: {set2}")   #set2不变
print(f"interSet is: {interSet}")

print(f"\nset 遍历")
for element in unionSet:
    print(f"set element is: {element}")

#作业：把一个list元素去重
print(f"\nlist元素去重")
numList = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3])
print(f"numList is: {numList}")
numSet = set()
for num in numList:
    numSet.add(num)
print(f"unique element is: {numSet}")


"""
Dict: 字典， { key1:value1,  key2:value2,  key3:value3}， 用逗号隔开的键值对
dict是无序的，不能用下标索引访问元素. 相同的key只能出现一次
"""
print("\n**************Dict**************")
mixDict = dict({
   "小明": {'chinese':80, 'math': 99},
   "小花": {'chinese':92, 'math': 95},
   "小红": {'chinese':85, 'math': 100}
})
print(f"mixDict is: {mixDict}, type is: {type(mixDict)}")
#用中括号访问字典,中括号内就是key
print(f"小明的成绩是: {mixDict['小明']}")
print(f"小明的数学成绩是: {mixDict['小明']['math']}")
#字典的新增和更新，如果key不存在就是add，如果存在就是更新
mixDict['小明'] = {'chinese':85, 'math': 97}
print(f"小明的成绩是: {mixDict['小明']}")
print(f"小明的数学成绩是: {mixDict['小明']['math']}")
mixDict['大牛'] = {'chinese':66, 'math': 77}
print(f"mixDict is: {mixDict}")
#删除元素
popElement = mixDict.pop('小明')
print(f"pop element is: {popElement}, mixDict is: {mixDict}")
#遍历:首先拿到全部key，然后一次遍历key就可以取到每个字典的value了
print(f"第一种dict遍历方式")
allKeys = mixDict.keys()
for key in allKeys:
    print(f"{key} = {mixDict[key]}")

print(f"第二种dict遍历方式")
#直接遍历字典，拿到的就是key
for key in mixDict:
    print(f"{key} = {mixDict[key]}")

#json 与 dict之间互相转换
import json
jsonStr = json.dumps(mixDict, ensure_ascii=False)
print(f"this is json string: {jsonStr}, it's type is: {type(jsonStr)}")
jsonStr = '{"小花": 170, "小红": 180, "大牛": 175}'
tallInfo = json.loads(jsonStr)
print(f"tall info is: {tallInfo}, tallInfo type is: {type(tallInfo)}")


print("\n**************打印99乘法表**************")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j}\t", end='')
    print()
