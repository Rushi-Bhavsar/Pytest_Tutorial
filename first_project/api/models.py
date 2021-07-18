from django.db import models


class EmployeeModel(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.emp_id}"


class EmployeeLoginModel(models.Model):
    punch_in = models.TimeField()
    punch_out = models.TimeField()
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee}"
