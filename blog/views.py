from django.shortcuts import render, redirect
from django.urls import reverse

from blog.forms import StudentForm
from blog.models import Student


# Create your views here.


def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def add_student(request):
    form = StudentForm(request.POST, request.FILES)

    if request.method == "GET":
        return render(request, "add_student.html", {"form": form})

    if form.is_valid():
        form.save()
        return redirect(reverse(students))
    return render(request, "add_student.html", {"form": form})
