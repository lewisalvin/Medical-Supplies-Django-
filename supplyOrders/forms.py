from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class FormPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["firstName", "lastName", "email", "insurance"]

   
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if Person.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email "%s" is already in use' % email)
    #     return email
