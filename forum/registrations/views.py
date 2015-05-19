from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from threads.views import side_bar_threads
from threads.models import Topic
# Create your views here.

#



def register(request):
    user_name = ''
    password1 = ''
    password2 = ''
    email = ''
    side_threads = side_bar_threads()
    topics = Topic.objects.all()

    if request.POST:
        user_name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        try:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, "Username already in use")
                return redirect('register')
        except User.DoesNotExist:
            pass

        if user_name and password1 and password2 and email:
            if password1 == password2:
                new_user = User()
                new_user.username = user_name
                new_user.password = password1
                new_user.email = email
                new_user.save()
                messages.success(request, "Success!")
                return redirect('/')
            else:
                messages.error(request, "Passwords do not match")
                return redirect('register')

        else:
            messages.error(request, "Please fill out all required fields")
            return redirect('register')

    return render(request, 'register.html', {
        'user_name': user_name, 'email': email, 'password1': password1,
        'password2': password2, 'side_threads': side_threads, 'topics': topics
    })