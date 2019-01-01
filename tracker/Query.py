from .models import  Employee
from django.core import serializers

class Query(object):
    
    class __Query():
        def __init__(self):
            pass

        def get_field_employees(self):       
            return serializers.serialize("json",Employee.objects.filter(extra_info__employee_type="employee"),fields=('pk','name','phone')) 

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