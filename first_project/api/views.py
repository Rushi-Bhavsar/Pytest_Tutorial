import datetime
from .models import EmployeeModel, EmployeeLoginModel
from .serializers import EmployeeModelSerializer, EmployeeLoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeAPI(ModelViewSet):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()


class EmployeeLoginAPI(APIView):

    def get(self, request):
        emp_id = request.data.get('employee')
        if emp_id is not None:
            emp_model_obj = EmployeeLoginModel.objects.filter(employee=emp_id)
            emp_serializer_obj = EmployeeLoginSerializer(emp_model_obj, many=True)
            return Response(emp_serializer_obj.data, status=status.HTTP_200_OK)
        emp_model_obj = EmployeeLoginModel.objects.all()
        emp_serializer_obj = EmployeeLoginSerializer(emp_model_obj, many=True)
        return Response(emp_serializer_obj.data, status=status.HTTP_200_OK)

    def post(self, request):
        emp_model_serializer_object = EmployeeLoginSerializer(data=request.data)
        if emp_model_serializer_object.is_valid():
            emp_model_serializer_object.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(emp_model_serializer_object.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.data.get('id')
        if pk is not None:
            emp_model_object = EmployeeLoginModel.objects.get(id=pk)
            emp_model_serializer_obj = EmployeeLoginSerializer(emp_model_object, data=request.data, partial=True)
            if emp_model_serializer_obj.is_valid():
                emp_model_serializer_obj.save()
                return Response({'msg': f'Record Updated for Primary key {pk}'}, status=status.HTTP_202_ACCEPTED)
            return Response(emp_model_serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.data.get('id')
        if pk is not None:
            print(pk)
            emp_model_object = EmployeeLoginModel.objects.get(id=pk)
            print(emp_model_object)
            emp_model_object.delete()
            return Response({'msg': f'Record {pk} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def data():
    emp_detail_list = []
    for employee in EmployeeModel.objects.all():
        emp_login_details = EmployeeLoginModel.objects.filter(employee=employee)
        total_time = datetime.timedelta()
        for item in emp_login_details:
            temp_time = lambda time_obj: datetime.datetime.combine(datetime.date(1, 1, 1), time_obj)
            temp_time_diff = temp_time(item.punch_out) - temp_time(item.punch_in)
            total_time = total_time + temp_time_diff
        emp_detail_list.append({'emp_id': employee.emp_id, 'working_hour': total_time, 'name': employee.name})
    return emp_detail_list


class EmployeeDetailsAPI(APIView):

    def get(self, request):
        emp_id = request.data.get('emp_id')
        emp_list = data()
        if emp_id is not None:
            for emp in emp_list:
                if emp.get('emp_id') == emp_id:
                    return Response(emp)
        return Response(emp_list)
