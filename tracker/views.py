from django.shortcuts import render
from .Query import Query
from django.http import JsonResponse
# Create your views here.

#view
def create_task(request):

    pass



def update_task(request):
    pass


def read_task(request):
    pass


def login(request):
    pass


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
     


