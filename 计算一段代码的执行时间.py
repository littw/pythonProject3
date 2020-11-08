import time
#
# start=time.time() #time模块里的time方法，获取当前时间戳
# #时间戳从1970-01——01 00:00:00 UTC~2020-11-06 12:01 UTC 中国是UTC+8
# print('start=',start)
# x=0
# for i in range(1,200000):
#     x+=i
# end=time.time()
# print('end=',end)
# print('代码耗时{}s'.format(end-start))


# def cal_time(fn):
#     start = time.time()  # time模块里的time方法，获取当前时间戳
#     fn()
#     end = time.time()
#     print('代码耗时{}s'.format(end - start))

def cal_time(fn):
    print('外部函数被调用')
    print('fn=',fn)
    # def inner():
    #     start=time.time()
    #     x=fn()
    #     end=time.time()
    #     print('代码执行的时间是：',(end - start))
    #     return x

    def inner(x,*args,**kwargs): #对原函数参数进行扩充
        start = time.time()
        s = fn(x)
        end = time.time()
        print('代码执行的时间是：', (end - start))
        return s,end-start
    return inner

# @cal_time   #第一调用cal_time，第二把装饰的函数传递给fn
# def demo():
#     x = 0
#     for i in range(1, 200000):
#         x += i
#     return x

@cal_time   #第一调用cal_time，第二把装饰的函数传递给fn
def demo(n):
    x = 0
    for i in range(1, 200000):
        x += i
    return x

@cal_time
def foo():
    print('hello')
    time.sleep(3)
    print('world')

x=demo(10000,'hello',y='good')
print(x)