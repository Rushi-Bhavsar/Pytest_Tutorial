from rest_framework import serializers
from .models import EmployeeModel, EmployeeLoginModel


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class EmployeeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLoginModel
        fields = '__all__'

    def validate_punch_in(self, value):
        if 10 > value.hour < 19:
            raise serializers.ValidationError('Punch In Time should be between 10:00AM and 20:00PM')
        return value

    def validate_punch_out(self, value):
        if 10 > value.hour < 19:
            raise serializers.ValidationError('Punch Out Time should be between 10:00AM and 20:00PM')
        return value
