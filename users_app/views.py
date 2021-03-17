from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomRegisterForm


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Account Created")
            return redirect("register")
    else:
        register_form = CustomRegisterForm()
    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)
