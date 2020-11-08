#有几个内置函数和内置类，用到了匿名函数
nums=[2,3,1,20,4]
#列表的sort方法，会直接对列表进行排序
nums.sort()
print(nums)
#sorted内置函数，不会改变原有的数据，而是生成一个新的结果
x=sorted(nums)
print(x)