from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name
