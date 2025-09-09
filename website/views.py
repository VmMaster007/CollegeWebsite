from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

# Login 
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

# Logout
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):

    my_records = Record.objects.all()
    context = {'Records':my_records}

    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'create_form':form}
    return render(request, 'pages/create_record.html',context=context)

# Update A Record
@login_required(login_url="login")
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    # if submitted data
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'update_form': form}
    return render(request, 'pages/update_record.html', context=context)

