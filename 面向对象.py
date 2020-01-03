# class Person(object):
#
#     def eat(self,food):
#         print('吃',food)
#
#     def sleep(self):
#         print('睡觉')
# a=Person()
# a.eat('米饭')
# a.sleep()

# class Person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def fun1(self):
#         print('self')
#         print('对象的属性是',self.name,self.age)
# # 实例化调用init,如果init中有除self之外的参数，那么实例化时需要传参
# a=Person('小mei',36)
# a.fun1()

# 定义一个学生类：Student，内部含有一个方法：study，实现打印：XX学习XX课程
class Student(object):
    def __init__(self,name):
        self.name=name
    def study(self,scor):
        self.scor=scor
        print('%s学习%s课程'%(self.name,scor))
        print(self.name+'学习'+scor+'课程')
        print(self.name,'学习',scor,'课程')

b=Student('小冉')
b.study('数学')