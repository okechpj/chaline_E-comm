from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    return render(request, 'login.html')

def register(request):
    if request == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Your account has been created!")

        return redirect('login')

    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')

def demo(request):
    return render(request, 'demo.html')