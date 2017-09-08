# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.URLField(max_length=600, blank=True)
    text = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title