"""
注解
前面讲的变量函数都没有注解，都是让python自动推导.
其实那样的代码不利于别人阅读和维护
"""


num = 3             #无注解定义法
num : int = 3       #有注解定义法

num2 = 2.5          #无注解定义法
num2 : float = 2.5  #有注解定义 法

#无注解定义法
def add (a, b):
    return a+ b

#有注解定义法
def add(a: int, b: int) -> int :
    return a+b

