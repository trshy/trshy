from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegisterForm, ChangePasswordForm


def login_view(request):
    nxt = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if nxt:
            return redirect(nxt)
        return redirect("/")
    return render(request, "form.html", {"form": form,
                                         "title": "Login",
                                         "type": "login"})


def register_view(request):
    next = request.GET.get('next')
    if request.user.is_authenticated:
        raise Http404
    form = UserRegisterForm(request.POST or None)
    context = {
        "form": form,
        "title": "Register",
        "type": "register",
    }
    if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data.get("username"),
                                        email=form.cleaned_data.get("email"),
                                        password=form.cleaned_data.get("password"))
        user.save()
        new_user = authenticate(username=user.username, password=form.cleaned_data.get("password"))
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", context)


def change_password_view(request):
    if not request.user.is_authenticated():
        raise Http404
    form = ChangePasswordForm(request.POST or None)
    context = {
        "form": form,
        "title": "Change Password",
        "type": "password",
    }
    print(form.is_valid())
    if form.is_valid():
        user = request.user
        user.set_password(form.cleaned_data.get("password"))
        user.save()
        new_user = authenticate(username=user.username, password=form.cleaned_data.get("password"))
        login(request, new_user)
        return redirect("/")
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

