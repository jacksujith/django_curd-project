from django import forms
from blogapps.models import Student 

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name","email","dept","address","phone_number")
