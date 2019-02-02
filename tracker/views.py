from django.shortcuts import render
from .Query import Query
from django.http import JsonResponse,HttpResponse,Http404
import json
import uuid
from .models import Task
from django.core import serializers
from rest_framework.exceptions import NotAuthenticated

# Create your views here.

def authenticate(function):
    def chek_authentication(request,*args,**kwargs):
        auth_token=request.META.get('HTTP_AUTHORIZATION')
        if(True):
            return function(request,1)
        else:
            return NotAuthenticated(detail="Forbiddion to access resource", code=403)    
    return chek_authentication    
#view

@authenticate
def create_task(request,employee_id):
    if request.method=='POST':
       task=request.body.decode('utf-8')
       task=json.loads(task) 
       q=Query()
       task=q.createTask(task)
       if not task.errors:
           return JsonResponse({"status":"success"},status=200) 
       else :
           return JsonResponse(task.errors,status=422) 


def update_task(request):
    pass


@authenticate
def read_task(request,employee_id):
    if request.method=='POST':
       q=Query()
       return JsonResponse(q.getTasks(employee_id,str(datetime.date.today())),safe=False)     
    else:
        return JsonResponse({"message":"mathod not allowed"},status=404)

def login(request):
    if request.method == 'POST':
        print(request.POST.get('username',None))
        print(request.POST.get('password',None))
        #
        #code of authentication
        #   
        return JsonResponse(uuid.uuid4(),safe=False)
    else:
        return JsonResponse({"message":"mathod not allowed"},status=404)

def update_gps(request):
    pass    


@authenticate
def get_gps_data(request,employee_id):
    if request.method == 'POST': 
        print(request.body)
        client_employee=request.POST.get('employee')
        date=request.POST.get('date')
        print(client_employee,date)
        q=Query()
        return JsonResponse(q.getGpsData(client_employee,date),safe=False)
    else:
        return JsonResponse({"message":"mathod not allowed"},status=404)
        
@authenticate
def create_gps_entry(request):
    gps_data=request.body.decode('utf-8')
    q=Query()
    serializer=q.creteGpsData(gps_data)
    if serializer.errors:
        return JsonResponse(serializer.errors,status=422) 
    return JsonResponse({"status":"success"},status=200)

def get_employee_id(request):
    pass

def get_field_employees(request):
    q=Query()
    return JsonResponse(q.getSerializedFieldEmployees(),safe=False)
