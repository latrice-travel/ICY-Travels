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
                return redirect('home')
    else:
        form = StudentLoginForm()
    context = {
        'form': form
    }
    return render(request, 'students/login.html', context)
