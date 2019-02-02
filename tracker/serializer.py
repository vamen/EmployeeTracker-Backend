from rest_framework import serializers
from .models import Task,Employee,TrackTable

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields='__all__'
    def validate_employee(self,attrs):  
            if attrs.extra_info['employee_type']=="admin":
                    raise serializers.ValidationError("wrong reques,requesting task of admin")
            return attrs
   
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=('pk','name','phone')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTable
        fields=('employee','date','lat','lang')    
            