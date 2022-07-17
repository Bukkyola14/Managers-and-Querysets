from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True, max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()

