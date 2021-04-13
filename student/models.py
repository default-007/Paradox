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


class clas(models.Model):
    Class_Choices = ((1, 'PP1'), (2, 'PP2'), (3, 'Grade 1'), (4, 'Grade 2'),
                     (5, 'Grade 3'), (6, 'Grade 4'), (7, 'Grade 5'), (8, 'Grade 6'))
    clas = models.PositiveSmallIntegerField(
        Class_Choices, null=True, blank=True)
    class_teacher = models.CharField(max_length=50)


class Subject(models.Model):
    name = models.CharField(max_length=200, blank=True)
    marks = models.IntegerField(blank=True, null=True)
    clas = models.ForeignKey(clas, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Exams(models.Model):

    name = models.CharField(max_length=200, blank=True)
    clas = models.ForeignKey(clas, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)


class Attendance(models.Model):
    pass
