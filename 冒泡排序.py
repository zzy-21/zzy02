s=[2,7,3,11,25,9,14,3]
# print(sorted(s))
# 冒泡排序
class Solution(object):
    def __init__(self,l):
        self.l = l

    def mp_sort(self):
        for i in range(len(self.l)):
            for j in range(len(self.l)-i-1):
                if self.l[j] > self.l[j+1]:
                    self.l[j+1], self.l[j]= self.l[j], self.l[j+1]
                else:
                    pass
        print(self.l)
P = Solution(s)
P.mp_sort()
for i in range(len(s)):
    for j in range(len(s)-1):
        if s[j]>s[j+1]:
            s[j+1],s[j]=s[j],s[j+1]
print(s)

L = [1,2,3,4,5]

map(str, L)
print(L)
