
'''
1、鼠标点住函数名+ctrl即可进入函数说明文档
2、help(函数名)运行即可进入说明文档
'''

#python里面的函数参数不限定类型，但是可以建议类型，当传入参数不符合建议类型，是参数会标黄但不会报错
def add(a:int,b:int):
    '''
    这个函数用来将两数相加并返回结果
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 结果
    '''
    c=a+b
    return c

result=add(1,4)
print(result**2)

y=add("Hello","World")#变黄会提示
#一个函数没有返回值，那么就返回None
x=print("hello")
print(x)

help(add)