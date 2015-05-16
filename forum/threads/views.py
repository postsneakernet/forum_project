from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply, Topic
# Create your views here.


def side_bar_threads():
    threads = Thread.objects.all()

    return threads[:10]


def thread(request, thread_slug):
    my_thread = get_object_or_404(Thread, slug=thread_slug)
    replies = Reply.objects.filter(thread=my_thread).values()
    return render(request, 'thread.html', {'replies': replies})


class Home(generic.ListView):
    template_name = 'Home.html'
    context_object_name = 'writers'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context

