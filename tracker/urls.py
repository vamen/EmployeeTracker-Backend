from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('fieldEmployees',views.get_field_employees,name="field_employees"),
    path('updateGps',views.update_gps,name="updategps")
]