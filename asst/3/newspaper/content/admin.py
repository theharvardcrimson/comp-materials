# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article,Contributor

admin.site.register(Article)
admin.site.register(Contributor)

# Register your models here.
