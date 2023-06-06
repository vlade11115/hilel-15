from django.urls import path

from . import views

urlpatterns = [
    path("", views.students, name="students_view"),
    path("add/", views.add_student, name="add_student_view"),
]
