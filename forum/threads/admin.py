from django.contrib import admin
from . import models

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ReplyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('created',)}



admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Reply, ReplyAdmin)
