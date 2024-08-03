from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.EmailField()
    state = models.CharField(max_length=30)
    phonenumber = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=30)
