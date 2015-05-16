from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply
# Create your views here.


def index(request):
    threads = Thread.objects.all()

    return render(request, 'index.html', {'threads': threads})

