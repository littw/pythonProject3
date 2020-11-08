def fun1():
    '''
    函数的内嵌，内嵌函数就相当于外函数的局部变量，不可以被直接调用
    :return:
    '''
    print('fun1正在被调用')
    def fun2():
        print("fun2正在被调用")
    fun2()

fun1()
#fun2()：无法直接调用

'''
LEGB原则：
L-Local：函数内的名字空间
E-Enclosing function locals:嵌套函数中外部函数的名字空间
G-Global：函数定义所在的模块的名字空间
B-Builtin：Python内置模块的名字空间
变量的查找顺序依次是：L->E->G->B
如下例
'''
x=88
def test():
    x=99
    def intest():
        x=11
        print(x)
    intest()
test()
print(x)

