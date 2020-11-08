
#1、关键字参数:传入实参时明确指定形参的变量名，其特点是参数之间不存在先后顺序
#调用函数时，位置参数必须要在关键字参数之前
def eat(somebody,something):
    print(somebody+" has eaten "+something)

eat("TongTong","fried chicken")
eat("Fried chicken","TongTong")
eat(somebody="TongTong",something="ice cream")
#eat(somebody="TongTong","ice cream"),这样会发生错误

#2、默认参数：允许为函数参数指定默认值，函数调用没有传递实参，则采用默认的参数值
def say_something(name="TongTong",word="I love python"):
     print(name+" has said that "+word)
say_something()
say_something("Mary","I love fish")

#def watch_movie(name='TongTong',beer=True,cigarrite=True,BF)
#函数定义当中，位置参数必须在默认参数之前

'''
3、收集参数(可变参数)：未调用函数之前并不知道要传进来多少个参数；
比如print()函数,如果是参个数不确定，定义函数时，形参就可以使用收集参数来搞定；
只需要在参数前面加上*号即可,如果在收集参数后面还需要指定其他的参数，呢么在调用函数的时候应该使用关键参数来指定，
否则将实参全部认为是收集参数；
'''

print(1,int(3),8+2,"hello")


def test(*params,extra):
    print("有%d个参数"%len(params))
    print("第二个参数是:",params[1])
    print("收集参数是：",params)
    print("位置参数是：",extra)

test('F','i','s','h','c',extra='.com')
#由运行结果看出，收集参数是以一个元组的形式存放的，函数定义中*起打包作用
#*在形参中起解包作用,如下例

#在元组中
num=(1,2,3,4)
print(*num)

#在字符串中
str="Fish"
print(*str)

#在列表中
list=['T','T','Y','Y']
print(list)
