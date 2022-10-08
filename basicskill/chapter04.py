"""
演示class的定义和使用
类有成员变量(属性)和成员函数(方法)
"""
import json

class Student:
    """
    声明student类，类里面封装了学生的基本信息
    """
    name = None     #姓名(公有,public)
    gender = None   #性别(公有,public)
    age = 0         #年龄(公有,public)
    favorite = None #爱好(公有,public)
    __weight = 0.0  #体重(私有,private)
    """
    构造函数会在创建对象时自动调用
    def __init__(self, name, gender, age, favorite):
        self.name = name
        self.gender = gender
        self.age = age
        self.favorite = favorite
    """


    def __str__(self):
        """
        self是成员函数定义时必须存在且放在第一个位置，使用时忽略这个参数.
        :return:
        """
        data = dict({"name": self.name, "gender": self.gender, "age": self.age, "favorite": self.favorite})
        return json.dumps(data, ensure_ascii=False)

    def isTeamSports(self):
        """
        喜欢的运动是否是团体运动.
        :return: true--是团体运动， false--不是团体运动
        """
        if (self.favorite == "足球" or
                self.favorite == "篮球" or
                self.favorite == "排球"):
            return True
        else:
            return False
        #return (self.favorite == "足球" or self.favorite == "篮球" or self.favorite == "排球")

    def sayHello(self, msg):
        """
        打招呼函数, 注意访问成员函数name，必须要加self., 传入的参数msg可以直接访问.
        :param msg:
        :return: None
        """
        print(f"hi {self.name}, {msg}")

    def __lt__(self, other):
        """
        比较函数 小于
        :param other:
        :return:
        """
        return self.age < other.age

    def __le__(self, other):
        """
        比较函数 小于等于
        :param other:
        :return:
        """
        return self.age <= other.age

    def __eq__(self, other):
        """
        等于比较函数 恒等于
        :param other:
        :return:
        """
        return self.name == self.name

    def setWeight(self, weight):
        """
        设置体重参数
        :param weight:
        :return:
        """
        self.__weight = weight

    def isOverWeight(self):
        """
        判断一个学生是否超重, 我们定义的标准是体重大于50公斤就超重.
        这里演示了成员函数可以访问私有属性
        :return:
        """
        return (self.__weight > 50)

# 使用类来创建对象
student1 = Student()
student1.name = "小m"
student1.gender = "男"
student1.age = 12
student1.favorite = "足球"
student1.setWeight(40)
print(f"student1 is: {student1}")
print(f"{student1.name} like {student1.favorite}, it's team sports: {student1.isTeamSports()}")
student1.sayHello("你很帅啊")


student2 = Student()
student2.name = "小h"
student2.gender = "女"
student2.age = 9
student2.favorite = "乒乓球"
student1.setWeight(49)
print(f"student2 is: {student2}")
print(f"{student2.name} like {student2.favorite}, it's team sports: {student2.isTeamSports()}")
student2.sayHello("可爱的小姑娘")


"""
student3 = Student("杨杨", "男", "14", "篮球")
print(f"student3 is: {student3}")
print(f"{student3.name} like {student3.favorite}, it's team sports: {student3.isTeamSports()}")
student3.sayHello("活波的男孩")
"""

student4 = Student()
student4.name = "小红"
student4.gender = "女"
student4.age = 10
student4.favorite = "网球"
student1.setWeight(51)
print(f"student2 is: {student4}")
print(f"{student4.name} like {student4.favorite}, it's team sports: {student4.isTeamSports()}")
student4.sayHello("可爱的小姑娘")



#两个对象可以比较大小得益于我们实现了魔术方法 __le__
if (student1 <= student2) :
    print(f"it's True")
else:
    print(f"it's False")

studentList = list([student1, student2, student4])
for student in studentList:
    print(f"{student.name} = {student.age}")

print(f"after sort")
studentList.sort()
for student in studentList:
    print(f"{student.name} = {student.age}")


class Phone:
    IMEI = "123" # 序列号
    producer = "Apple" # 厂商

    def radioType(self):
        """
        返回手机支持的无线通信网路是几代的，例如2g, 3g, 4g, 5g
        :return:
        """
        return "2g"

class IPhone6(Phone):
    """
    IPhone4继承自Phone, 它具有父类的属性
    """
    faceID = "2016" #支持了面部识别

    def radioType(self):
        return "4g"


class NFCReader:
    """
    nfc读写类
    """
    def readNFC(self):
        print(f"read nfc")

    def writeNFC(selfs):
        print(f"write nfc")

class RemoteController:
    """
    遥控器类
    """
    def doRemoteControl(self):
        print(f"do remote control")


class IPhone14(IPhone6, NFCReader, RemoteController):
    """
    多继，phone14有了很多功能,包括nfc和遥控器
    """

    IMEI = "456"

    def radioType(self):
        """
        重写了父类的函数
        :return:
        """
        return "5g"

    def getIMEI(self):
        print(f"parent's imei: {super().IMEI}")
        return self.IMEI

iphone14 = IPhone14()
print(f"radio version: {iphone14.radioType()}")
print(f"call readNFC: {iphone14.readNFC()}")
print(f"call remote controller: {iphone14.doRemoteControl()}")
print(f"call getIMEI: {iphone14.getIMEI()}")

class Animal:
    def bark(self) -> None :
        """
        pass表示空，即：没有实现，实现任务交给子类来实现。
        这个函数即使抽象函数，有抽象函数的类叫抽象类。抽象类不能被用来创建对象.
        :return:
        """
        pass

class Dog(Animal):
    """
    Animal有个抽象函数bark，子类必须自己来实现，否则会报错
    """
    def bark(self) -> None:
        print(f"汪汪汪")

class Cat(Animal):
    def bark(self) -> None:
        print(f"喵喵喵")

def doBark(animal: Animal) -> None:
    """
    这个函数参数是animal，所有animal的子类都可以作为参数传进来.
    这就是面向对象里的多态
    :param animal:
    :return:
    """
    animal.bark()

dog : Dog = Dog()
cat : Cat = Cat()
doBark(cat)
doBark(dog)


"""
总结
1. 类的属性就是成员变量, 行为就是成员函数;
2. 类就像图纸，对象就根据图纸生产出来的具体产品. 这就是面向对象的简单概念.
3. 常用的魔术方法, __str__, __init__, __eq__, __le__;

"""