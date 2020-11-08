
#开放封闭原则：已经写好的功能代码能不改就不改

def can_play(fn):
    def inner(x,y,*args,**kwargs): #kwargs是一个字典
       # print(args)
       # if args[0]<22:
       #      fn(x,y)
       clock=kwargs['clock']
       clock=kwargs.get('clock',23)    #用户不给时间，默认不认玩
       if clock<=22:
           fn(x,y)
       else:
            print('太晚了，赶紧睡觉啊')

    return inner


@can_play
def play_game(name,game):
    print('{}正在玩{}'.format(name,game))

play_game('lily','jump and jump',clock=18)
play_game('lily','jump and jump',clock=23)