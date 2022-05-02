from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class FormPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["firstName", "lastName", "passwd", "confirmpasswd", "email", "insurance"]


class LoginPerson(forms.Form):
    email = forms.CharField(label="Email", max_length=100)
    passwd = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=20)