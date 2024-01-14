from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from verify_email.email_handler import send_verification_email
from  notes.models import *
from django.contrib.auth import get_user_model
from .helpers import delete_not_activated_users
def register(request):
    if request.method == "GET":
        form  = RegisterForm()
        return render(request, "authentication/register.html", {"form" : form})
    else:
        form = RegisterForm(request.POST)
        delete_not_activated_users()
        if form.is_valid():
            instance = form.save(commit=False)
            if get_user_model().objects.filter(email = instance.email) or \
                get_user_model().objects.filter(username=instance.username):
                return redirect("Note:error",msg = "sorry username or email already exist")
            inactive_user = send_verification_email(request, form)
            print(inactive_user.is_active)
            return redirect("authentication:login", send_verfication="OK")
        return redirect("Note:error", msg = "sorry something is wrong please try again")
def login_user(request, send_verfication=None):
    print("not here")
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "authentication/login.html", {"form" : form, "send_verfication" : send_verfication})
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
                return redirect("Note:error", msg="sorry try to login again")
        return redirect("Note:error", msg ="username or password is wrong")
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
