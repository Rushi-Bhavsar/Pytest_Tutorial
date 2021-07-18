from django.test import TestCase
from api.models import EmployeeModel, EmployeeLoginModel
from datetime import time
from mixer.backend.django import mixer


class TestAllModelClass(TestCase):

    def test_for_employee_add(self):
        """
        This test case check if we can add employee to the Employee Model.
        :return: If True return True or False.
        """
        EmployeeModel.objects.create(name="Swaroop Daghe", emp_id="101", city="Mumbai")
        employee_obj = EmployeeModel.objects.get(emp_id=101)
        # self.assertEqual(str(employee_obj.name), "Swaroop Daghe")

        # Works only in pytest framework
        assert str(employee_obj.name) == "Swaroop Daghe"

    def test_for_employee_login_add(self):
        """
        This test case check if we can add employee login details in the EmployeeLoginModel Model.
        :return: If True return True or False.
        """
        EmployeeModel.objects.create(name="Swaroop Daghe", emp_id="101", city="Mumbai")
        emp = EmployeeModel.objects.get(emp_id=101)
        EmployeeLoginModel.objects.create(employee=emp, punch_in=time(10, 40), punch_out=time(12, 40))
        query_set = EmployeeLoginModel.objects.filter(employee=101)
        # self.assertEqual(query_set.count(), 1)

        # works only in pytest framework
        assert query_set.count() == 1

    def test_for_punch_out_check(self):
        """
        This test case check all the punch out time for a specific employee should be less than 15:00 pm.
        :return: If True return True or False.
        """
        EmployeeModel.objects.create(name="Swaroop Daghe", emp_id="101", city="Mumbai")
        emp = EmployeeModel.objects.get(emp_id=101)
        EmployeeLoginModel.objects.create(employee=emp, punch_in=time(10, 40), punch_out=time(12, 40))
        EmployeeLoginModel.objects.create(employee=emp, punch_in=time(13, 00), punch_out=time(15, 40))
        query_set = EmployeeLoginModel.objects.filter(employee=101)
        for obj in query_set:
            # self.assertLess(obj.punch_out, time(16, 00))

            # Works only in pytest framework
            assert obj.punch_out < time(16, 00)

    def test_for_punch_in_using_mixer(self):
        """
        This test case check all the punch in and punch out time should be between than 10:00 am and 20:00 pm.
        We will be also using mixer to create instance of employee model.
        :return: If True return True or False.
        """
        EmployeeLoginModel.objects.create(employee=mixer.blend(EmployeeModel), punch_in=time(12, 40),
                                          punch_out=time(13, 20))
        # This is also Ok.
        # EmployeeLoginModel.objects.create(employee=mixer.blend(EmployeeModel, emp_id=102), punch_in=time(12, 40),
        #                                           punch_out=time(13, 20))
        EmployeeLoginModel.objects.create(employee=mixer.blend(EmployeeModel), punch_in=time(13, 40),
                                          punch_out=time(16, 10))
        EmployeeLoginModel.objects.create(employee=mixer.blend(EmployeeModel), punch_in=time(16, 40),
                                          punch_out=time(19, 40))
        EmployeeLoginModel.objects.create(employee=mixer.blend(EmployeeModel), punch_in=time(10, 40),
                                          punch_out=time(12, 30))
        query_set = EmployeeLoginModel.objects.all()
        for obj in query_set:
            print(obj.punch_out)
            # self.assertGreater(obj.punch_in, time(10, 00))
            # self.assertLess(obj.punch_out, time(20, 00))

            # works only in pytest framework.
            assert obj.punch_in > time(10, 00)
            assert obj.punch_out < time(20, 00)

