'''
读取data文件中的数据，将所有的数字去重并按照从小到大的顺序写入backup文件
1.读取data文件中的数据
2。去掉换行符
3.去重
4.从小到大排列
5.写入新文件backup文件中
'''
s=[]
f=open('/Users/zhaozhenyu/zzy/data2.txt','r')
m=f.readlines()
m=[x.strip() for x in m if x.strip()!='']
print(m)
n=[int(j) for j in m ]
print(n)
for h in n:
    if h not in s:
        s.append(h)
s.sort()
print(s)
a=open('/Users/zhaozhenyu/zzy/backup.txt','w')
a.writelines(' '.join(str(s)))
f.close()
a.close()

'''
11，10，18
2，23，24
22，1，0
13，7
5
29，19
10，1，3，5，9
将大列表中的换行符去掉
将每个元素拆分成子列表，转化为数值型
合并子列表去重，按从小到大排序
'''
# import re
# file_read=open('/Users/zhaozhenyu/zzy/data3.txt','r')
# file_write=open('/Users/zhaozhenyu/zzy/data4.txt','w')
#
# full_list=[]
# new_list=[]
# new_list1=[]
# fileContentList=file_read.readlines()
# for line in fileContentList:
#     line=line.strip('\n')
#     if len(line.strip('\n'))==0:
#         continue
#     line=re.split('[，|]+',line)
#     full_list=full_list+line
#
#     print(line)
# full_list=list(set(full_list))
#
# for j in full_list:
#     h=int(j)
#     new_list. append(h)
# new_list=sorted(new_list)
#
# for i in new_list:
#     n=str(i)
#     new_list1. append(n)
# print(new_list1)
#
# file_write.writelines(' '.join(new_list1))
# file_write.close()
# file_read.close()
#
