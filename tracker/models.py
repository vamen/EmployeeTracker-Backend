from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone=models.CharField(max_length=10,unique=True)
    extra_info=JSONField()

    def __str__(self):
        return self.name

class Employee_authentication(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    password=models.CharField(max_length=255)
    salt=models.CharField(max_length=255)
    token=models.CharField(db_index=True,max_length=255,default="None")
       

    def __str__(self):
        return self.employee.name

class Task(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    task_heading=models.CharField(max_length=255)
    task_detail=models.TextField()
    address=models.TextField()
    lat=models.CharField(max_length=25)
    lang=models.CharField(max_length=25)
    status=models.CharField(max_length=255)

    def __str__(self):
        return self.employee.name+" : "+self.task_heading

class TrackTable(models.Model):
      employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
      date=models.DateField()
      track_field=JSONField()  

      def __str__(self):
          return self.employee.name + " : "+self.date.__str__()

