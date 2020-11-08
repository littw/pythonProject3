'''
函数三要素：函数名 参数 返回值
一些编程语言中云U型函数充满，在python里面不允许
函数重名了，后一个函数会覆盖前一个函数
python函数名也可以理解为一个变量名，变量与函数同名也会覆盖掉函数名
'''
def test(a,b):
    return a+b
def test(a,b):
    return a-b
def test(a):
    return a**2

print(test(1,2))