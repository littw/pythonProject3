# def discount(price,rate):
#     final_price=price*rate
#     #print("在函数中访问全局变量original_price："+original_price )
#     original_price=100
#     print("在函数中修改Original_price:%.2f"%original_price)
#     return final_price
#
# original_price=float(input("请输入原价:"))
# rate=float(input("请输入折扣率："))
# final_price=discount(price=original_price,rate=rate)
# print(type(final_price))
# print("打折后的价格是：%.2f"%final_price)
# print("全局中Original_price：%2f"%original_price)

'''
global可以在函数中修改全局变量的值
'''
count=5
print('修改前%d'%count)
def myfun():
    '''
    在函数中修改全局变量count的值
    :return:
    '''
    global count
    count=10
    print('在函数中修改：%d'%count)
myfun()
print('修改后：%d'%count)
count=8
print("在全局修改：%d"%count)
