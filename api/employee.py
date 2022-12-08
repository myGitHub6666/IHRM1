# 封装接口
import requests

# 创建接口类
import config
from config import BASE_URL


class EmployeeApi():
    def __init__(self):
        # 员工添加的接口
        self.url_get_emp = BASE_URL + '/api/sys/user'
        self.url_update_emp = BASE_URL + '/api/sys/user/{}'
        self.url_select_emp = BASE_URL + '/api/sys/user/{}'
        self.url_delete_emp = BASE_URL + '/api/sys/user/{}'

    # 员工添加
    def get_employees(self, add_emp_data):
        return requests.post(url=self.url_get_emp, json=add_emp_data, headers=config.header_data)

    # 员工查询
    def post_employee(self, id):
        return requests.get(url=self.url_select_emp, headers=config.header_data)

    # 员工修改
    def put_employee(self, id, update_emp_data):
        url = self.url_update_emp.format(id)
        return requests.put(url=url, json=update_emp_data, headers=config.header_data)

    # 员工删除
    def delete_employee(self,id):
        url=self.url_delete_emp.format(id)
        return requests.delete(url=url, headers=config.header_data)
