# 1.type类型函数
# a=1
# b=2.4
# c='happy'
# print(type(a))
# print(type(b))
# print(type(c))

# input
# str=input('请输入一个参数')
# print(str)

# 输出格式
d=3
e=4.5
f='sad'
print('d的值为：%d , e的值为%f , f的值为%s'%(d,e,f))
print('d的值为{},e的值为{},f的值为{}'.format(d,e,f))
print(f'd的值为: {d},e的值为:{e},f的值为:{f}')
print('d的值为%f , e的值为%03f , f的值为%s'%(d,e,f))


s=[]
for a in range(2,11):
    isPrime=True
    for b in range(2,a):
        if a%b==0:
            isPrime=False
            break
    if isPrime:
        s.append(a)
print(s)
