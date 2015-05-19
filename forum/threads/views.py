from datetime import datetime
from django.contrib import messages
from django.db.models import Count
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from .models import Thread, Reply, Topic

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

    def get_context_data(self, error="", **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        context['error'] = error
        return context

    def get_queryset(self):
        return Thread.objects.all()[:5].annotate(reply_count=Count('reply__id'))


class TopicIndex(generic.ListView):
    template_name = 'topic_index.html'
    context_object_name = 'topics'

    def get_context_data(self, **kwargs):
        context = super(TopicIndex, self).get_context_data(**kwargs)
        context['side_threads'] = side_bar_threads()
        return context

    def get_queryset(self):
        return Topic.objects.annotate(thread_count=Count('thread__id'))


class TopicDetail(generic.ListView):
    template_name = 'topic_detail.html'
    context_object_name = 'threads'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, slug=self.kwargs['topic_slug'])
        context['side_threads'] = side_bar_threads()
        context['topics'] = Topic.objects.all()
        return context

    def get_queryset(self):
        return Thread.objects.filter(topic__slug=self.kwargs['topic_slug']).annotate(reply_count=Count('reply__id'))


def thread_detail(request, topic_slug, thread_slug):
    thread = get_object_or_404(Thread, slug=thread_slug)
    replies = Reply.objects.filter(thread=thread)
    side_threads = side_bar_threads()
    topics = Topic.objects.all()

    if request.POST:
        new_reply = Reply()
        author = request.POST.get('author')
        if author:
            new_reply.author = author

        new_reply.thread = thread
        body = request.POST.get('body')
        if body:
            new_reply.body = body
            new_reply.save()
            messages.success(request, "New comment successfully added!")
        else:
            messages.error(request, "Oops, there was an error adding comment.")
        return redirect('thread_detail', topic_slug, thread_slug)

    return render(request, 'thread_detail.html', {
            'thread': thread, 'replies': replies, 'topics': topics,
            'side_threads': side_threads,
    })


def create(request):
    topics = Topic.objects.all()
    side_threads = side_bar_threads()

    if request.POST:
        new_thread = Thread()
        author = request.POST.get('author')
        title = request.POST.get('title')
        topic_id = request.POST.get('topic_id')
        body = request.POST.get('body')
        if title and topic_id and body:
            slug = slugify(title)

            if Thread.objects.filter(slug=slug).exists():
                messages.error(request, "Oops, there was an error creating thread.")
                return redirect('create')

            if author:
                new_thread.author = author

            new_thread.title = title
            new_thread.slug = slug

            new_thread.body = body
            new_thread.topic = Topic.objects.get(id=topic_id)
            new_thread.save()
            messages.success(request, "New thread successfully created!")
            return redirect('/')
        else:
            messages.error(request, "Oops, there was an error creating thread.")
            return redirect('create')


    return render(request, 'create.html', {
            'topics': topics, 'side_threads': side_threads,
    })