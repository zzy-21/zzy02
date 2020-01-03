'''
想得到多重嵌套中的数是2的倍数的平方组成的list
'''
list1=[[1,2,3],[4,5,6],[7,8,9],[10]]
list2=[]
# for i in list1:
#     for j in i:
#         if j%2==0:
#             squ=j**2
#             list2.append(squ)
# print(list2)
# # 变成列表推导式：
# list2=[j**2 for i in list1 for j in i if j%2==0]
# print(list2)
'''
想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
'''
# for i in list1:
#     if len(i)>1:
#         for j in i:
#             if j%2==0:
#                 squ=j**2
#                 list2.append(squ)
# print(list2)
# 列表推导式：list2=[j**2 for i in list1 for j in i if len(i)>1 if j%2==0] print(list2)

'''
练习：列出100以偶数中能整除3的所有数字
'''
# for i in range(1,101):
#     if i%2==0 and i%3==0:
#         list2.append(i)
# print(list2)
list2=[i for i in range(1,101) if i%2==0 and i%3==0]
print(list2)
