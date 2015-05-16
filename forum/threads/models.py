from django.db import models

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    # title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Thread)

    def __str__(self):
        return self.slug
