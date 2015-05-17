from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def most_recent_thread(self):
        return Thread.objects.filter(topic=self)[:1]

    def __str__(self):
        return self.title


class Thread(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=50, default="anonymous")
    topic = models.ForeignKey(Topic)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Reply(models.Model):
    author = models.CharField(max_length=50, default="anonymous")
    thread = models.ForeignKey(Thread)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = "replies"

    def __str__(self):
        return str(self.id) + " re: " + self.thread.title

