from django.urls import path
from . import views
from .views import read_task

urlpatterns = [
    path('login', views.login, name='login'),
    path('fieldEmployees',views.get_field_employees,name="field_employees"),
    path('updateGps',views.update_gps,name="updategps"),
    path('tasks',read_task,name="read_tasks"),
    path('create_tasks',views.create_task,name="create_tasks"),
    path('read_gps',views.get_gps_data,name="read_tasks"),
    path('update_gps',views.create_gps_entry,name="create_gps")
   
]