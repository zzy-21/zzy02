import myfun
import unittest
# 类名不能与关键字同名，类中有几个test开头的方法就有几个测试用例

class testAdd(unittest.TestCase):
    def test_add(self):
       result= myfun.add(4,5)
       self.assertAlmostEqual(8,result)

if __name__ == '__main__':
    unittest.main()
