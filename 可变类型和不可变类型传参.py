def test(a):
    a=100

def demo(nums):
    nums[0]=10

x=1
print(x)
print('x修改之前的地址是0x%x'%id(x))
test(x)
print('x修改之后的地址是0x%x'%id(x))
print(x)

a=[0,1,2,3,4]
print(a)
print('a修改之前的地址是0x%x'%id(a))
demo(a)
print(a)
print('a修改之前的地址是0x%x'%id(a))