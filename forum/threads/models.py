from django.db import models

# Create your models here.

class Subject(models.Model):
    subject = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Thread(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return self.title


class Reply(models.Model):
    # title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    thread = models.ForeignKey(Thread)

    def __str__(self):
        return self.slug
