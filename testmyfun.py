def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b


class MyTestCase(object):

    def test_add1(self,a,b):
        add1=a+b
        print('--1',add1)
    def test_add2(self,a,b):
        add2=a+b
        print('--2',add2)
