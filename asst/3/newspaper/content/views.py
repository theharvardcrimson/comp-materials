# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article, Contributor
from django.views import generic

num_articles=Article.objects.all().count()
num_authors=Contributor.objects.all().count()

def index(request):
    position = 0
    output = []
    temporary = []
    for art in Article.objects.all():
        temporary.append(str(art.title))
        temporary.append("http://127.0.0.1:8000/page/article/"+str(position+1))
        output.append(temporary)
        temporary = []
        position += 1
    return render(
        request,
        'index.html',
        context={'data':output,'num_authors':num_authors,'num_articles':num_articles},
    )

def articleListView(request, pk):
    ipk = int(pk)-1
    if ipk < num_articles:
        articleObject = Article.objects.all()[ipk]
        contributors = ""
        for elmt in articleObject.contributors.all():
            contributors+=str(elmt.show())
            contributors+=', '
        contributors = contributors[:-2]
        return render(
            request,
            'article_template.html',
            context={'contributors':contributors,'title':articleObject.title,'subtitle':articleObject.subtitle,'date':articleObject.pub_date,'text':articleObject.text},
        )
    else:
        return render(
            request,
            'not_found.html',
            context={'num_articles':num_articles},
        )
# Create your views here.
