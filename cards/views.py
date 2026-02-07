from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def user_login(request):
    if request.user.is_authenticated:
        return redirect("generator")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("generator")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "cards/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def generator(request):
    return render(request, "cards/generator.html")
