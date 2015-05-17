from datetime import datetime
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply, Topic
from django.db.models import Count
import operator


def month_delta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and not y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)


def side_bar_threads():
    max = datetime.now();
    min = month_delta(max, -1)
    threads = Thread.objects.filter(created__range=(min, max)).annotate(reply_count=Count('reply__id'))

    order = sorted(threads, key=operator.attrgetter('reply_count'), reverse=True)
    return order[:10]


class Home(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'threads'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context

    def get_queryset(self):
        return Thread.objects.order_by('created')[:5]


class TopicIndex(generic.ListView):
    template_name = 'topic_index.html'
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super(TopicIndex, self).get_context_data(**kwargs)
        context['side_threads'] = side_bar_threads()
        return context

    def get_queryset(self):
        return Topic.objects.all()


class TopicDetail(generic.ListView):
    template_name = 'topic_detail.html'
    context_object_name = 'threads'

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs['topic_slug'])
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context

    def get_queryset(self):
        return Thread.objects.filter(topic__slug=self.kwargs['topic_slug'])


def thread_detail(request, topic_slug, thread_slug):
    thread = get_object_or_404(Thread, slug=thread_slug)
    replies = Reply.objects.filter(thread=thread)
    side_threads = side_bar_threads()
    topics = Topic.objects.all()

    if request.POST:
        reply = request.POST.get("body", "replier", )
        new_reply = Reply()
        new_reply.body = reply[0]
        new_reply.replier = reply[1]
        new_reply.save()

    return render(request, 'thread_detail.html', {
            'thread': thread, 'replies': replies, 'topics': topics,
            'side_threads': side_threads,
            })