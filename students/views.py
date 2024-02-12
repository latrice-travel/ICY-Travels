from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from students.forms import StudentLoginForm, StudentSignUpForm
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = StudentLoginForm()
    context = {"form": form}
    return render(request, "students/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


def signup_view(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_Data["password_confirmation"]
            if password == confirm:
                user = User.objects.create_user(username, password=password)
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "The passwords do not match")
    else:
        form = StudentSignUpForm()
    context = {"form": form}
    return render(request, "students/signup.html", context)
