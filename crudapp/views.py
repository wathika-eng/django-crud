from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    return render(request, "crudapp/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    context = {"form": form}
    return render(request, "crudapp/register.html", context)


def my_login(request):
    user_json = "anonymous"
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, message="Logged in successfully")
                return redirect("dashboard")
            else:
                messages.warning(request, "Invalid username or password")
            user_json = json.dumps(user)

    context = {"form": form, "user": user_json}

    return render(request, "crudapp/login.html", context=context)


def my_logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {"records": my_records}
    return render(request, "crudapp/dashboard.html", context=context)


@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully")
            return redirect("dashboard")
    context = {"form": form}

    return render(request, "crudapp/create_record.html", context=context)


@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "crudapp/update_record.html", context=context)


@login_required(login_url="login")
def single_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {"record": all_records}
    return render(request, "crudapp/view_record.html", context=context)


def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record deleted!")
    return redirect("dashboard")


def error_404_view(request, exception):
    return redirect("dashboard")
