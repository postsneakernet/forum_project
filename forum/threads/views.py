from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply, Topic
# Create your views here.


def side_bar_threads():
    threads = Thread.objects.all()

    return threads[:10]

#
# def thread(request, thread_slug):
#     my_thread = get_object_or_404(Thread, slug=thread_slug)
#     replies = Reply.objects.filter(thread=my_thread).values()
#     return render(request, 'thread.html', {'replies': replies})


class Home(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'home'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context


class Topics(generic.ListView):
    template_name = 'topics.html'
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super(Topics, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['side_threads'] = side_bar_threads()
        return context


class ThreadIndex(generic.ListView):
    template_name = 'thread_index.html'
    context_object_name = 'thread_index'

    def get_context_data(self, **kwargs):
        context = super(ThreadIndex, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['topics'] = Topic.objects.all()
        context['side_threads'] = side_bar_threads()
        return context

class ThreadDetail(generic.ListView):
    template_name = 'thread_detail.html'
    context_object_name = 'thread_detail'

    def get_context_data(self, **kwargs):
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['topics'] = Topic.objects.all()
        context['side_threads'] = side_bar_threads()
        return context
