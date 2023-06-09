import uuid

from django.db import models


# Create your models here.


def upload_certificate(instance, filename):
    return f"certificates/{uuid.uuid4()}/{filename}"


class Student(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    certificate = models.ImageField(upload_to=upload_certificate, null=True)

    def __str__(self):
        return self.name
