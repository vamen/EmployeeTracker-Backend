from django.shortcuts import render
from .Query import Query
from django.http import JsonResponse,HttpResponse,Http404
import json
import uuid
from .models import Task
from django.core import serializers

# Create your views here.

#view
def create_task(request):

    pass



def update_task(request):
    pass


def read_task(request):
    auth_token=request.META.get('HTTP_AUTHORIZATION')
    # TEMP code
    data=eval(serializers.serialize("json",Task.objects.all()))
    lst=[]
    if len(data)>0:
        for items in data: 
            lst.append(items['fields'])

    return JsonResponse(lst,safe=False)

def login(request):
    if request.method == 'POST':
        print(request.POST.get('username',None))
        print(request.POST.get('password',None))
        #
        #code of authentication
        #   
        return JsonResponse(uuid.uuid4(),safe=False)
    else:
        raise Http404("method not allowed")


def update_gps(request):
    pass    


def get_gps_data(request):
    pass


def create_gps_entry():
    pass

def get_employee_id(request):
    pass

def get_field_employees(request):
    q=Query()
    print(q.get_field_employees())
    return JsonResponse(q.get_field_employees(),safe=False)
     


