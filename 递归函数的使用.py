
#函数内部自己调用自己
#递归要有出口

count=0
def test():
    global count
    count+=1
    print('hello')
    if count<5:
        test()

test()

#递归求1-n的和
def get_sum(n):
    if n==0:
        return 0
    return  get_sum(n-1)+n


print(get_sum(5))

#递归求n!
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(4))

#递归求斐波那契函数
def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))