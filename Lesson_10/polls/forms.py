from .models import User
from django.forms import ModelForm
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    number = forms.IntegerField( help_text = "Enter 6 digit roll number" )
    password = forms.CharField(widget = forms.PasswordInput()) 

    
class StudentForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'phone'] # “__all__”