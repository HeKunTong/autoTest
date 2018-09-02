import unittest
from case.login import Login
import HTMLTestRunner

if __name__ == "__main__":
    testUnit = unittest.TestSuite()
    testUnit.addTest(Login('inputUserName'))
    testUnit.addTest(Login('userNotExist'))
    testUnit.addTest(Login('inCorrectUser'))
    testUnit.addTest(Login('loginSuccess'))

    filename = 'D:\\autoTest\\login.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'微信管理系统测试报告',
        description = u'用例执行情况：'
    )
    # 运行测试用例
    runner.run(testUnit)
    fp.close()