from django.db import models

# Create your models here.


class Student(models.Model):
    names = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.IntegerField(blank=True, null=True)
    adm_no = models.CharField(max_length=20, blank=True, null=True)
    residence = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    stream = models.CharField(max_length=250, null=True, blank=True)
    clas = models.CharField(max_length=250, null=True, blank=True)
