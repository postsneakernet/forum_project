from datetime import datetime
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Thread, Reply, Topic
from django.db.models import Count
import operator
# Create your views here.

def month_delta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and not y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)


def side_bar_threads():
    max = datetime.date.now();
    min = month_delta(max, -1)
    threads = Thread.objects.filter(created__range=(min, max)).annotate(reply_count=Count('reply__id'))

    order = sorted(threads, key=operator.attrgetter('reply_count'), reverse=True)
    return order[:10]


class Home(generic.ListView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context

    def get_queryset(self):
        return Thread.objects.all()


class TopicIndex(generic.ListView):
    template_name = 'topic_index.html'
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super(TopicIndex, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        context['side_threads'] = side_bar_threads()
        return context

    def get_queryset(self):
        return Thread.objects.all()


class TopicDetail(generic.ListView):
    template_name = 'topic_detail.html'
    context_object_name = 'thread_index'
    # topic_slug = None
    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['topics'] = Topic.objects.all()
        context['topic'] = self.topic_slug

        context['side_threads'] = side_bar_threads()
        return context

    def get_queryset(self):
        return Thread.objects.all()


class ThreadDetail(generic.ListView):
    template_name = 'thread_detail.html'
    # context_object_name = 'thread_detail'

    def get_context_data(self, **kwargs):
        context = super(ThreadDetail, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.order_by('created')[:5]
        context['topics'] = Topic.objects.all()
        context['side_threads'] = side_bar_threads()
        return context

    def get_queryset(self):
        return Thread.objects.all()
