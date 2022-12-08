# 创建测试用例
import unittest

from api.employee import EmployeeApi
from utils import common_assert


class TestEmployee(unittest.TestCase):
    employeeid = 1288026500225929216

    def setUp(self):
        self.employee = EmployeeApi()

    def tearDown(self):
        pass

    def testAddEmployee(self):
        add_emp_data = {
            "username": "小新3",
            "mobile": "13501110031",
            # "timeOfEntry":'2020-09-23',
            "formOfEmployment": 1,
            "workNumber": "0121",
            # "departmentName":"销售",
            # "departmentId":"1266699057968001024",
            # "correctionTime":'2020-09-25T13:00:00. 000Z'

        }
        response = self.employee.get_employees(add_emp_data=add_emp_data)
        # TestEmployee.employeeid = response.json().data().get('id')
        # TestEmployee.employeeid = response.json().data().get('id))
        common_assert(self, response, 200, True, 10000, "操作成功")

    def testUpdateEmployee(self):
        update_emp_data = {
            "username": "小新3",
        }
        response = self.employee.put_employee(id=TestEmployee.employeeid, update_emp_data=update_emp_data)
        print(response.json())

        common_assert(self, response, 200, True, 10000, "操作成功")

    def testSelectEmployee(self):
        response = self.employee.post_employee(id=TestEmployee.employeeid)
        print(response.json())
        # TestEmployee.employeeid = response.json().data().get('id))
        common_assert(self, response, 200, True, 10000, "操作成功")

    def testDeleteEmployee(self):
        response = self.employee.delete_employee(id=TestEmployee.employeeid)
        print(response.json())
        # TestEmployee.employeeid = response.json().data().get('id))
        common_assert(self,response,200,True,10000,"操作成功")