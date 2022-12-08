# 导包
import time
import unittest
from scripts.test01_login import TestLogin
# 组装测试套件
from scripts.test02_login import TestLoginPrm
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestLoginPrm))
# 指定测试报告的路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report,"wb") as f:
    runner = HTMLTestRunner(f,title="API report")
    # 创建HTMLTestRunner运行器
    # 执行测试套件
    runner.run(suite)
