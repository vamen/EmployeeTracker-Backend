from .models import  Employee,Task,TrackTable
from django.core import serializers
from django.db import transaction

from .serializer import TaskSerializer,EmployeeSerializer,TrackSerializer

class Query(object):
    
    class __Query():
        def __init__(self):
            pass

        def getSerializedFieldEmployees(self):   
            employees=Employee.objects.filter(extra_info__employee_type="employee")    
            return  EmployeeSerializer(employees,many=True).data


        def getEmployeeFromToken(self,token):
            try:
                return Employee_authentication.objects.get(token=token)
            except Exception:
                return   

        def getTasks(self,employee,date):
            task=Task.objects.filter(employee=employee,date=date)
            task=TaskSerializer(task,many=True)
            return  task.data
           

        def createTask(self,task_data):
            task=TaskSerializer(data=task_data)
            if task.is_valid():
                task.save()
            return task
               
        def creteGpsData(self,gps_datas):
            serialize=TrackSerializer(data=gps_datas,many=True)
            if serialize.is_valid():
                serialize.save()
            return serialize    
        
        def getGpsData(self,employee,date):
            gpsEntries=TrackTable.objects.filter(employee=employee,date__lte=date)    
            return TrackSerializer(gpsEntries,many=True).data

    single_instance=None
    
    def __init__(self):
        if not Query.single_instance:
               Query.single_instance=Query.__Query()

    
    def __getattr__(self, name):
        return getattr(self.single_instance, name)
    
    def __setattr__(self, name):
        return setattr(self.single_instance, name)


if __name__ == "__main__":
    q=Query()
    q.get_field_employees()