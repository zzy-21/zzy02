#coding:utf-8
# list1=[1,2,3,4,3,4,2,5,5,8,9,7]
# for a in list1:
#         flg=tr
#         if list1.count(num)>1:
#             list1.remove(a)
# print(list1)
# # a=2
# # a*=3+3
# # print(a)
# #
# # list2=[i*i for i in range(1,11)]
# # print(list2)
#
# # 想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# # exmaple5 = [j**2 for i in example2 if len(i)>1 for j in i if j%2 == 0]
# list4=[]
# for i in example4:
#     if len(i)>1:
#         for j in i:
#             if j%2==0:
#                 a =j**2
#                 list4.append(a)
# print(list4)
#
# # # 列出100以内偶数中能整除3的所有的数字
# # for i in range(1,101):
# #     if i%2==0 and i%3==0 :
# #         print (i)
# list5=[i for i in range(1,101) if i%2==0 and i%3==0 ]
# print(list5)

# def num(a,b):
#     a,b=input("输入两个参数：",).split(',')
#     print(int(a)+int(b))
#     print(int(a) - int(b))
#     print(int(a) *int(b))
#     print(int(a) /int(b))
# num(1,6)
# def num1(a,b):
#     a, b = input("输入两个参数：", ).split(',')
#     c=input("输入符号：")
#     if c=='+':
#         print(int(a) + int(b))
#     elif c=='-':
#         print(int(a) - int(b))
#     elif c=='*':
#         print(int(a) * int(b))
#     elif c=='/':
#         print(int(a) / int(b))
#     else :
#         print('输入有误！')
# num1(2,3)

# def add_end(l=None):
#     if l is None:
#         l=[]
#         l.append('END')
#         return l
# print(add_end())
# print(add_end())

# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError as result:
#         print(result)
# a=int(input('-'))
# b=int(input('-'))
# calc(a,b)

# def calc(a,b):
#     try:
#         print(a/b+c)
#     except (ZeroDivisionError ,NameError ) as result:
#         print(result)
# a=int(input('请输入'))
# b=int(input('输入'))
# calc(a,b)

# def calc(a,b):
#     try:
#         print(a/b)
#     except Exception as result:
#         print(result)
#     else:
#         print('程序没有异常')
#     finally:
#         print('程序执行结束')
# a=int(input('请输入'))
# b=int(input('请输入'))
# calc(a,b)


# f=open('D:\zzy\zzy02\data.txt','r')
# f.write("hhheehhe")
# print(f.write())
# print(f.read())
# print(f.read(3))
#读取整行
# print(f.readline())
#读取所有行，作为一个数列输出
# print(f.readlines())
# f.close()


# f=open('D:\zzy\zzy02\data.txt','w+')
# f.write("hhheehhe")
# m=['hello','\npython']
# f.writelines(m)
# f.seek(0)
# print(f.read())
# f.close()

# f=open('D:\zzy\zzy02\data.txt','r')
# f.readlines()
# m=[f.readlines()]
# print(m)
# 读出后排序，然后写入文件
# a=open('D:\zzy\zzy02\data2.txt','w')
# a.write(m)
# m.close()

# 从小到大排列，并写入backup
# m=[f]
# m.sort()
# a=open('D:\zzy\zzy02\data2.txt','w')
# a.write(m)

# 导入目标模块
import mymonlde
mymonlde.fun1()
# 使用from..import导入
from mymonlde import *
fun1()
from mymonlde import fun1
fun1()
# 包的导入
# from mymondle import


