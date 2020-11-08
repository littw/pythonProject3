#def 函数名(参数)：
#   函数要执行的操作

#调用函数：函数名(参数)
def tell_story(person1,person2):
    print(person1+"在给"+person2+"故事")

tell_story(person2="小杨",person1="小刘")

person1=input("\nWho will tell the story?")
person2=input("Who will listen the story?")
tell_story(person1,person2)