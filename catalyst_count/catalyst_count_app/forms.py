from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        widgets={'username':forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
                'first_name':forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}),
                 'last_name':forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}),
                 'email': forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
                 'password':forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"})}

