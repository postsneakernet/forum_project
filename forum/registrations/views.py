from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

#
def register(request):
    # if request.POST:
    #     new_user = User()
    #     user_name = request.POST.get('name')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     email = request.POST.get('email')
    #
    #     if user_name and password1 and password2 and email:
    #         if password1 == password2:
    #             pass

    return render(request, 'register.html',
        # {
        # 'user_name': user_name, 'email': email, 'password1': password1,
        # 'password2': password2,}
    )