from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_content, name ='content_index'),
    url(r'^articles/$', views.article_index, name ='articles/article_index'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.single_article, name='articles/single_article'),
    url(r'^contributors/$', views.contributor_index, name ='contributors/contributor_index'),
    url(r'^contributors/(?P<contributor_id>[0-9]+)/$', views.single_contributor, name='contributors/single_contributor'),
    url(r'^images/$', views.image_index, name ='images/image_index'),
    url(r'^images/(?P<image_id>[0-9]+)/$', views.single_image, name='images/single_image'),
]