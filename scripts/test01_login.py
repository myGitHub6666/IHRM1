# 导包
import unittest

import config
from api.login import LoginAPI


# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = LoginAPI()

    # 后置处理
    # def tearDown(self):
    #     pass
    # 定义测试用例
    # case001 登录成功
    def test01_case001(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000003", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        # 获取TOKEN值
        config.TOKEN ="Bearer " + response.json().get("data")
        print(config.TOKEN)
        # 给hearder+dada里面追加值
        config.header_data['Authorization'] = config.TOKEN
        print(config.header_data)

    # case002 不输入手机号
    def test02_case002(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case003 不输入密码
    def test03_case003(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "password": ""})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case004 手机长度小于11位
    def test04_case004(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "1380000000", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case005 手机号长度大于11位
    def test05_case005(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "138000000012", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # 定义测试用例
    # case006 手机号输入非数字
    def test06_case006(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "error", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case007 输入未注册手机号
    def test07_case007(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13812343212", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case008 参数异常-多参数。程序健壮性不错的话应该是成功的
    def test08_case008(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "haha": "heihei"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # case009 缺少手机号
    def test09_case009(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case010 缺少密码
    def test10_case010(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # case11 无参
    def test11_case011(self):
        # 调用登录接口进行登录
        response = self.login_api.login(None)
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(99999, response.json().get("code"))
        self.assertIn("抱歉，系统繁忙，请稍后重试！", response.json().get("message"))

    # case12 错误参数-手机号
    def test12_case012(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobie": "13800000002", "password": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))
    # case13 错误参数——密码参数错误
    def test13_case013(self):
        # 调用登录接口进行登录
        response = self.login_api.login({"mobile": "13800000002", "pssword": "123456"})
        print(response.json())
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))
