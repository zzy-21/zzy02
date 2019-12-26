# 1.string.capitalize(),把字符串的第一个字母大写
s='hello,python!!!'
print(s.capitalize())

# 2.string.count(str, beg=0, end=len(string))，返回str在string里面出现的次数，如果beg或者end指定,则返回指定范围内str出现的次数
print(s.count('h',2,len(s)))
print(s.count('p',0,len(s)))

# 3.string.find(str, beg=0, end=len(string)),检查str是否包含在string中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print(s.find('w',0,len(s)))
print('l',3,len(s))

# 4.string.isalpha(),如果string至少有一个字符并且所有字符都是字母则返回True，否则返回False
a='weweeweweqe'
print('string.isalpha()中全部都是字符:',a.isalpha())
print('string.isalpha()中包含特殊字符:',s.isalpha())

# 5.string.isdigit(),如果string中只包含数字返回True，否则返回False
digit='123232423'
print('string.isdigit()中不包含数字:',s.isdigit())
print('string.isdigit()中包含数字:',digit.isdigit())

# 6.string.join(seq),以string为分隔符，将seq中所有的元素（的字符串表示）并合并为一个新的字符串
h='*'
print('string.join(seq)用*来分隔：',h.join(s))

# 7.string.replace(str1, str2,  num=string.count(str1)),将string中的str1，替换为str2,如果num指定，则不超过num次数
print('替换次数不超过num值：',s.replace('o','AAA',1))
print('替换次数超过num值：',s.replace('o','BBBB',4))

# 8.string.split(str="", num=string.count(str)),以str为分隔符切片string，如果指定num值，则仅分隔num+个字符串

print(s.split('h',2))

# 9.string.strip([obj]),在string上之行lstrip()和rstrip()
x='\hqeqweqweqw\h'
print(x.rstrip('\h'))
print(x.lstrip('\h'))
'''
练习：有这样一个文件，文件内容如下：
Lucy|18601914231|男|19890218
Jack|18101913132|女|19810311
Tom|18201912533|女|19830713
Lily|18301911734|男|19870210

任务1-找出所有L开头的人名
任务2-按照年龄进行排序
任务3-找出所有女性用户的信息

'''
f=open('/Users/zhaozhenyu/zzy/data1.txt','r+')
x='\n'
m=[]
for i in f.readlines():
    if x not in i:
        m.append(i)
    else:
        i = i.strip(x)
        m.append(i)
print(m)
'''任务1-找出所有L开头的人名
# 读取列表中的每个元素
# 判断每个元素的首字母
# 追加首字母为L到新列表中，打印新列表
'''
name=[]
for n in range(len(m)):
    if 'L' in m[n]:
        name.append(i)
print(name)
'''任务2-按照年龄进行排序
# 取出每个字符串的长度，再取每个字符串的倒数8位字符串
# 比较8位字符串的大小，排序
'''
from datetime import datetime
k=[]
b=[]
for j in range(len(m)):
    str=m[j]
    a=int(str[-8:len(m[j])])
    k.append(a)
    k.sort()
print(k)

'''
判断每个元素中是否有"女"，追加到新列表中，打印新列表
'''

sex=[]
for j in range(len(m)):
    if '女' in m[j]:
        sex.append(m[j])
print(sex)

f.close()



