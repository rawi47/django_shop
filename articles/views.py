from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Article



def index(request):
    articles = Article.objects.order_by('name')
    template = loader.get_template('articles/index.html')
    context = {
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'articles/detail.html', {'article': article})
