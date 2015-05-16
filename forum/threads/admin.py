from django.contrib import admin
from . import models
from .models import Thread, Reply

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ReplyAdmin(admin.ModelAdmin):
    pass
    # reply = Reply.objects.get(pk=id)
    # thread = reply.thread.slug + '_' + str(id)
    # prepopulated_fields = {'slug': ('',)}


admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Reply, ReplyAdmin)
