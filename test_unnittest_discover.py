import unittest
import unittest ,HTMLTestRunner
# 创建测试套件，并将符合条件的test开头的方法添加到其中


discover=unittest.defaultTestLoader.discover('/Users/zhaozhenyu/PycharmProjects/zzy02/', pattern='testmyfun.py')
print('------discover',discover)



# 实例化texttestRunner
runner=unittest.TextTestRunner()
# 调用run方法运行测试条件
# runner.run(discover)

# suite=unittest.TestSuite()
# suite.addTest(myTest('test_add'))


filename='/Users/zhaozhenyu/PycharmProjects/zzy02/test.html'
fp=open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='单元测试 ',description='我的描述')
runner.run(discover)
fp.close()

