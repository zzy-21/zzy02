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
'''
分析思路：
1.房子类
1.1房子属性：户型，总面积，家具列表，剩余面积
1.2添加家具，打印房子信息及家具内容
2.家具类
2.1家具属性：名字，家具尺寸
'''
class House():
    # 户型 apartment，总面积 area，剩余面积 resarea
    def __init__(self,apartment,area,resarea):
        self.apartment=apartment
        self.area=area
        self.resarea=resarea
        # self.size=size
    def L(self):
       # self.size=Furniture()
       # self.area = self.resarea + self.size
       print('户型%s，总面积%.2f，剩余面积%.2f'%(self.apartment,self.area,self.resarea))

class Furniture():
    def __init__(self,name,size):
        self.name=name
        self.size=size
    def furnList(self,name,size):
        print('%s，占%.1f平米'%(self.name,self.size))
a=House('三室一厅',100,34)
a.L()
b=Furniture('床',4)
b.furnList('床',4)

