# 登录接口的封装
# 导包
import requests


# 定义接口类
import config


class LoginAPI:
    # 初始化类
    def __init__(self):
        self.url = config.BASE_URL+"/api/sys/login"
        # self.url = "http://ihrm-java.itheima.net/api/sys/login"

    # 定义接口调用方法
    def login(self, login_data):
        return requests.post(url=self.url, json=login_data)
