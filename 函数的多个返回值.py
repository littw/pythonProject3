

def test(a,b):
    '''

    :param a:
    :param b:
    :return: 返回两个值，将两个值以元组的形式返回，
    除了元组，还可以用列表，字典等的形式进行多值返回
    '''
    x=a//b
    y=a%b
    return x,y#实际返回的是一个元组(x,y)

result=test(12,4)
print("商是{}，余数是{}".format(result[0],result[1]))

shang,yushu=test(30,7)
print("商是{}，余数是{}".format(shang,yushu))
