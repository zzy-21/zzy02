'''
1.定义一个列表
2.从键盘上驶入一个数
3.判断该数是否在列表中，如果在，打印happy，元素内的值加1，如果不在，打印sad

'''
list1=[1,2,4,6,8,9]
a=int(input('请输入一个数'))
if a in list1:
    n=list1.index(a)
    list1[n]+=1
    print('happy',list1)

else:
    print('sad')

'''
1.输入一个数，判断该数的范围：90-100：等级为A。。。。60一下：等级为E

'''
a=int(input('请输入一个数：'))
if 90<a<=100:
    print('等级为A：',a)
elif 80<a<=90:
    print('等级B：',a)
elif 70<a<=80:
    print('等级为C：',a)
elif 60<a<=70:
    print('等级为D：',a)
else:
    print('等级为E:',a)