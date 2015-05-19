from django.shortcuts import render

from threads.views import side_bar_threads
from threads.models import Topic


def login(request):
    side_threads = side_bar_threads()
    topics = Topic.objects.all()

    return render(request, 'login.html', {
            'side_threads': side_threads, 'topics': topics,
    })
