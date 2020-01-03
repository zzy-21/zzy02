
'''
导入ddt包
2.用装饰器装饰ddt
3.传入参数，执行
'''

import unittest
from ddt import ddt,data,unpack

# 第一种传参方式
@ddt
class MyTestCase1(unittest.TestCase):
    @data(1)
    def test_normal(self,value):
        print(value)
        self.assertEqual(value,1)
#
# 2,3,4会分别按照执行次数传入，比如第一次执行传入2，第二次执行方法传入3
#     @data(2,3,4)
#     def test_normal(self,value):
#         print(value)
#         self.assertEqual(value,2)
if __name__ == '__main__':
    unittest.main()