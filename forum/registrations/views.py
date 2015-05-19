from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

#
def register(request):
    if request.POST:
        user_name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if user_name and password1 and password2 and email:
            if password1 == password2:
                new_user = User()
                new_user.username = user_name
                new_user.password = password1
                new_user.email = email
                new_user.save()
                messages.success(request, "Success!")
            else:
                messages.Error(request, "Passwords do not match")
                return redirect('register')

        else:
            messages.Error(request, "Please fill out all required fields")
            return redirect('register')



    return render(request, 'register.html', {
        'user_name': user_name, 'email': email, 'password1': password1,
        'password2': password2,
    })