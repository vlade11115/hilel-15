from django.shortcuts import render

from blog.models import Student


# Create your views here.


def index(request):
    return render(request, "index.html")


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})
