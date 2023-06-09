from django.forms import ModelForm

from blog.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ("name", "city", "certificate")
