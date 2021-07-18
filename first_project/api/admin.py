from django.contrib import admin
from .models import EmployeeModel, EmployeeLoginModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'emp_id', 'city']


@admin.register(EmployeeLoginModel)
class EmployeeLoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'punch_in', 'punch_out', 'employee']
