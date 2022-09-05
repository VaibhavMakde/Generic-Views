from django.db import models


# Create your models here.
class Grade(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    mark = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    graduated = models.BooleanField(default=True)
    grades = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=70)
