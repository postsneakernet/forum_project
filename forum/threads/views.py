from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply
# Create your views here.


def thread(request, thread_slug):
    my_thread = get_object_or_404(Thread, slug=thread_slug)
    replies = Reply.objects.filter(thread=my_thread).values()
    return render(request, 'thread.html', {'replies': replies})


class ForumIndex(generic.ListView):
    template_name = 'writers.html'
    context_object_name = 'writers'
    template_name = 'index.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ForumIndex, self).get_context_data(**kwargs)
        context['thread'] = Thread.objects.all()
        context['replies'] = Reply.objects.all()
        return context


def index(request):
    threads = Thread.objects.all()

    return render(request, 'index.html', {'threads': threads})


c