from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormPerson, ValidationError
from django.contrib import messages

from .models import Person

def home(request):
    thisPerson = Person.objects.all
    return render(request, 'home.html', { 'person': thisPerson,})

def login(request):
    form = FormPerson(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        if Person.objects.filter(email=email).exists():
            #raise ValidationError('Email "%s" is already in use' % email)
            messages.error(request, "Email already in use pleigh boy!")
            return redirect("login")
        #return email
        form.save()

    context = {'form': form }
    
    return render(request, 'home.html', context)

def test(request):
    useremail = ""

    form = FormPerson(request.POST)
    if form.is_valid():
        useremail = form.cleaned_data.get("email")
        try:
            user=Person.objects.get(email=useremail)
            context = {'form': form, 'error': 'Email already taken my boy!'}
            return render(request, 'test.html', context)
        except Person.DoesNotExist:
            form.save()
            context = {'form': form}

            return render(request, 'test.html',)
