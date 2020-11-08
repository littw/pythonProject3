# 除了使用def关键字定义一个函数以外，我们饿还可以使用lambda表达式定义一个函数
#匿名函数
# 用来表达一个简单的函数，函数调用的次数很少，基本上就是调用一次
# 调用匿名函数两种方式：
# 1、给他定义一个名字 很少使用
# 2、把函数当作参数传给另一个函数
mul=lambda a, b: a + b
print(mul(3,4))

def calc(a,b,fn):
    return fn(a,b)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# print(calc(2, 3, add))
# print(calc(8, 2, sub))

print(calc(3,2,lambda x,y:x+y))
print(calc(3, 2, lambda x, y: x * y))
print(calc(3,2,lambda x,y:x-y))
print(calc(3, 2, lambda x, y: x / y))




