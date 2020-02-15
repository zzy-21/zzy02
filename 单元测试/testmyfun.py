from testmyfun import *
import unittest
# 类名不能与关键字同名，类中有几个test开头的方法就有几个测试用例

class TestMyFun(unittest.TestCase):
    # TestCase基类方法，所有case执行前自动执行
    # TestCase基类方法，所有case执行之后自动执行
    @classmethod
    def setUpClass(cls):
        print('这里是所有测试用例前的准备工作')

    # TestCase基类方法，所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print('这里是所有测试用例后的清理工作')

    # TestCase基类方法，每次执行前自动执行
    def setUp(self):
        print('这里是一个测试用例前的准备工作')

    # TestCase基类方法，每次执行case后自动执行
    def tearDown(self):
        print('这里是一个测试用例后的清理工作')
    @unittest.skip('想临时调过这个测试用例')
    def test_add(self):
        self.assertEqual(3,add(1,2))
        # self.assertNotEqual(3,add(2,2))

    def test_minus(self):
        # self.skipTest('跳过这个测试用例')
        self.assertEqual(1,minus(3,2))

    def test_multi(self):
        self.assertEqual(6,multi(2,3))

    def test_divide(self):
        self.assertEqual(2.5,divide(5,2))

if __name__ == '__main__':

    unittest.main(verbosity=2)
