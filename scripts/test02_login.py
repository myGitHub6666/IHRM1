# 导包
import json
import os
import unittest
from api.login import LoginAPI
from parameterized import parameterized


def build_data():
    log_data = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    file = os.path.join(base_dir,'../data/data.json')
    print(file)
    with open(file, encoding="utf-8") as f:
        file_data = json.load(f)
        for data in file_data:
            login_data = data.get('login_data')
            status_code = data.get('status_code')
            success = data.get('success')
            code = data.get('code')
            message = data.get('message')
            log_data.append((login_data, status_code, success, code, message))
            # print('log_data={}'.format((login_data, status_code, success, code, message)))
    return log_data


# 创建测试类
class TestLoginPrm(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = LoginAPI()

    # 后置处理
    # def tearDown(self):
    #     pass
    # 定义测试用例
    # case001 登录成功
    @parameterized.expand(build_data)
    def test_login(self, login_data, status_code, success, code, message):
        # 调用登录接口进行登录
        response = self.login_api.login(login_data)
        print(response.json())
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))
