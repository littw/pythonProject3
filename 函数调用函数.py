def test1():
    print("test1开始了")
    print("test1结束了")

def test2():
    print("test2开始了")
    test1()
    print("test2结束了")

#计算[m,n)之间的整数和
def add(m,n):
    x=0
    for i in range(m,n):
        x+=i

#计算n的阶乘
def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
#计算阶乘和
def factorial_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=factorial(i)
    return sum


print(factorial_sum(3))