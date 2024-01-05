from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from  notes.models import *
def register(request):
    if request.method == "GET":
        form  = RegisterForm()
        return render(request, "authentication/register.html", {"form" : form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authentication:login")
        print("wtf")
        return redirect("Note:error", msg = "sorry something is wrong")
def login_user(request):
    print("not here")
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "authentication/login.html", {"form" : form})
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user.is_authenticated:
                login(request, user)
                return redirect("Note:main")
            else:
                return redirect("Note:error", msg="sorry u are dumb")
        return redirect("Note:error", msg ="form is not valid")
@login_required
def logout_user(request):
    logout(request)
    return redirect("Note:main")
@login_required
def profile(request):
    user = request.user
    number_of_notes = Note.objects.filter(user = user).count()
    number_of_vaults = Vault.objects.filter(user=user).count()
    return render(request, "authentication/profile.html", {"number_of_notes" : number_of_notes, "number_of_vaults"
                                                           : number_of_vaults, "email" : user.email})
