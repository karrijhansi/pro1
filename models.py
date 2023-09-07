from django.db import models
class StudentsData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=50)
    fee=models.IntegerField()
    dob=models.DateField()
    location=models.CharField(max_length=50)


# Create your models here.
