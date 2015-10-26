from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Article, Image, Contributor, Content
# Create your views here.

def all_content(request):
	content_list = Content.objects.order_by('-pub_date')[:10]
	template = loader.get_template('content_index.html')
	context = RequestContext(request, {
        'content_list': content_list,
    })
	return HttpResponse(template.render(context))

def article_index(request):
	latest_article_list = Article.objects.order_by('-pub_date')[:10]
	template = loader.get_template('articles/article_index.html')
	context = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
	return HttpResponse(template.render(context))

def single_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/single_article.html', {'article': article})

def contributor_index(request):
	contributors_list = Contributor.objects.order_by('last_name')[:10]
	template = loader.get_template('contributors/contributor_index.html')
	context = RequestContext(request, {
        'contributors_list': contributors_list,
    })
	return HttpResponse(template.render(context))

def single_contributor(request, contributor_id):
    contributor = get_object_or_404(Contributor, pk=contributor_id)
    return render(request, 'contributors/single_contributor.html', {'contributor': contributor})

def image_index(request):
	images_list = Image.objects.order_by('-pub_date')[:10]
	template = loader.get_template('images/image_index.html')
	context = RequestContext(request, {
        'images_list': images_list,
    })
	return HttpResponse(template.render(context))

def single_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'images/single_image.html', {'image': image})
