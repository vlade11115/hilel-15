from django.urls import path

from . import views

urlpatterns = [
    path("", views.students, name="students_view"),
]
