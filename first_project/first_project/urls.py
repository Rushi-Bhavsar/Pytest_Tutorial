from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EmployeeAPI, EmployeeDetailsAPI, EmployeeLoginAPI

router = DefaultRouter()
router.register('employee', EmployeeAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('emp_login/', EmployeeLoginAPI.as_view()),
    path('emp_details/', EmployeeDetailsAPI.as_view())
]
