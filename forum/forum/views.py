from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from threads.views import side_bar_threads
from threads.models import Topic


def login_user(request):
    side_threads = side_bar_threads()
    topics = Topic.objects.all()

    if request.POST:
        username = request.POST['name']
        password =  request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "You have been logged in")
                return redirect('home')
        else:
            messages.error(request, "Oops, there was a problem logging in ")
            return redirect('login')

    return render(request, 'login.html', {
            'side_threads': side_threads, 'topics': topics,
    })

def logout_user(request):
    if request.POST:
        logout(request)
        messages.success(request, "You have been logged out")

    return redirect('home')