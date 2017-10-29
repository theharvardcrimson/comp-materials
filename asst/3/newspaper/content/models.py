# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    def show(self):
        print(self.title)
        if self.subtitle:
            print(self.subtitle)
        print(self.pub_date)
        for e in self.contributors.all():
            e.show()
        print(self.text)

class Contributor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def show(self):
        fullName = str(self.first_name)+' '+str(self.last_name)
        return(fullName)
    def die(self):
        self.delete()
