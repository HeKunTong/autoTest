import unittest
from case.account import Account
import HTMLTestRunner

def accountCase(testUnit):
    testUnit.addTest(Account('upload'))

if __name__ == "__main__":
    testUnit = unittest.TestSuite()
    accountCase(testUnit)

    filename = 'D:\\autoTest\\resources\\report\\account.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'微信管理系统测试报告',
        description = u'用例执行情况：'
    )
    # 运行测试用例
    runner.run(testUnit)
    fp.close()