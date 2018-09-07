import unittest
from case.fileArea import FileArea
import HTMLTestRunner

def fileAreaCase(testUnit):
    testUnit.addTest(FileArea('upload'))
    testUnit.addTest(FileArea('edit'))

if __name__ == "__main__":
    testUnit = unittest.TestSuite()
    fileAreaCase(testUnit)

    filename = 'D:\\autoTest\\resources\\report\\fileArea.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'微信管理系统测试报告',
        description = u'用例执行情况：'
    )
    # 运行测试用例
    runner.run(testUnit)
    fp.close()