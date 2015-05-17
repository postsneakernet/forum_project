from django.contrib import admin
from . import models


class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "thread_count", "created")
    prepopulated_fields = {'slug': ('title',)}

    def thread_count(self, instance):
        threads = models.Thread.objects.filter(topic__slug=instance.slug)
        return threads.count()


class ThreadAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "topic", "reply_count", "created")
    prepopulated_fields = {'slug': ('title',)}

    def reply_count(self, instance):
        replies = models.Reply.objects.filter(thread__slug=instance.slug)
        return replies.count()


class ReplyAdmin(admin.ModelAdmin):
    list_display = ("author", "thread", "thread_topic", "created")

    def thread_topic(self, instance):
        return instance.thread.topic


admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Reply, ReplyAdmin)
