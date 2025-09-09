from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {'login_form':form}
    return render(request,'pages/login.html', context=context)

def register(request):
    # make a form from forms.py
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return(form)
    context = {'form' : form}

    return render(request, 'pages/register.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'pages/dashboard.html')