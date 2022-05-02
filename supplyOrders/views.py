from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FormPerson, ValidationError, LoginPerson
from django.contrib import messages
from django.contrib.auth import logout as logouts


from .models import Person

def home(request):
    thisPerson = Person.objects.all
    return render(request, 'home.html', { 'person': thisPerson,})

def register(request):
    form = FormPerson(request.POST)
    thisPerson = Person.objects.all
    
    context = {'form': form }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        passwd = form.cleaned_data.get('passwd')
        confirmpasswd = form.cleaned_data.get('confirmpasswd')
        if Person.objects.filter(email=email).exists():
            #raise ValidationError('Email "%s" is already in use' % email)
            messages.error(request, "Email already in use pleigh boy!")
            return redirect("register")
        if passwd != confirmpasswd:
            messages.error(request, "Your passwords don't match mane!")
            return redirect("register")
        #return email
        form.save()
        return render(request, 'home.html', {'person': thisPerson,})

    
    
    return render(request, 'register.html', context)

def login(request):
    if request.POST:
        form = LoginPerson(request.POST)
        
    else:
        form = LoginPerson()
    
    if form.is_valid():
        email = form.cleaned_data.get('email')
        passwd = form.cleaned_data.get('passwd')
        thisPerson = Person.objects.filter(email=email)
        
        
        if Person.objects.filter(email=email).filter(passwd=passwd).exists():
            return render(request, 'home.html', {'person': thisPerson})
        else:
            messages.error(request, "Your email or password is wrong as hell.  Try again!")
            return render(request, 'login.html', {'form': form})
        
    return render(request, 'login.html', {'form': form})
    


def logout(request):
    if request.method == 'POST':
        logouts(request)
        return redirect('login')
