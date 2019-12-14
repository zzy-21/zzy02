

# r方式打开文件data2.txt
# f=open('/Users/zhaozhenyu/zzy/zzy02/data2.txt','r')
# 读取多行数据，放在列表中
# print(f.readlines())
# 去除换行符
# f=f.strip('\n')
# 定义一个新数列，放去重后的数列，排列大小
# m=[]
# for  i in f:
#     if i not in m:
#         m.append(i)
# # m.sort()
# h = open('/Users/zhaozhenyu/zzy/zzy02/backup.txt', 'w+')
# print(h.writelines(m))
#
# # f.close()
# # 写入backup文件

# h.close()

# a、定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
# 定义学生类
class Student():
    # 定义study方法
    def study(self,name,kc):
        print('%s学习%s课程' % (name,kc))
#调用Student类
s=Student()
# 调用Student类中的方法study
s.study('小明','数学')

# b、定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
# 定义学生类
class Student():
    def __init__(self,sno,kc):
        self.sno=sno
        self.kc=kc
    def study(self):
        print('学号为%s的学生，学习%s课程'%(self.sno,self.kc))
a=Student('1110','语文')
a.study()
# 定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
# 1、实现gh为xx的老师，教xx课
# 2、实现gh为xx老师，在xx上班，一月工资xx
# 3、名字是xx，工号为xx的老师，吃饭
class Person():
    def eat(self):
        print('吃饭')
class Teacher(Person):
    def __init__(self,gh,school,kc,selary,name):
        self.__gh=gh
        self.kc=kc
        self.school=school
        self.selary=selary
        self.name=name
    def teach(self):
        print('gh为%s的老师，教%s课程'%(self.__gh,self.kc))
        print('gh为%s的老师，在%s上班，一月工资%d'%(self.__gh,self.school,self.selary))
        print('名字为%s,工号为%s的老师'%(self.name,self.__gh))

b=Teacher('1234','English','清华',10000,'小明')
b.teach()
b.eat()

# 1、打印小猫爱吃鱼，小狗要喝水
# class Animal():
#     def __init__(self,animalName):
#         self.animalName=animalName
#     def live(self):
#         self.eat()
#         self.drink()
#     def drink(self):
#         print("%s要喝水" % self.animalName)
#
# class Cat(Animal):
#     def __init__(self):
#         self.name = '小猫'
#         super(Cat, self).__init__(self.name)
#     def eat(self):
#         print("%s爱吃鱼"%self.name)
#
# class Dog(Animal):
#     def __init__(self):
#         self.name = '小狗'
#         super(Dog, self).__init__(self.name)
#     def eat(self):
#         print("%s爱吃肉"%self.name)
#
# animal=Cat()
# animal.live()
# animal=Dog()
# animal.live()


# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
# 定义一个People类，有属性name和weight，方法每次跑步，每次吃东西
class People():
    def __init__(self,pname,pweight):
        self.pname=pname
        self.pweight=pweight
    def everytime(self):
        print('每次跑步会减肥0.5公斤')
        print('每次吃东西体重会增加1公斤')
    def weigth(self):
        print('%s体重%d公斤'%(self.pname,self.pweight))

class Ming(People):
    def __init__(self):
        self.name='小明'
        self.weight=75
        super(Ming, self).__init__(self.name,self.weight)
    def run(self):
        print('%s爱跑步，爱吃东西'%self.name)

class Mei(People):
    def __init__(self):
        self.name='小美'
        self.weight = 45
        super(Mei, self).__init__(self.name,self.weight)

xiaoming=Ming()
xiaoming.weigth()
xiaoming.run()
xiaoming.everytime()
xiaomei=Mei()
xiaomei.weigth()

# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表



# class House():
#     # def __init__(self):
#     #     self.apar=apar
#     #     self.area=area
#     #     self.fur=fur
#     def jiaju(self):
#         self.bed()
#         self.closet()
#         self.table()
# class jiaju(House):
#     def bed(self):
#         print('床：占4平米')
#     def closet(self):
#         print('衣柜：占2平米')
#     def table(self):
#         print('餐桌：占1.5平米')
# house=House()
# house.jiaju()

#
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量








