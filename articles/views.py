from django.shortcuts import render
from .models import Article
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id): 
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Article not found.')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Article not found.')

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)) )

def single(request):
    try:
        a = Article.objects.order_by('-pub_date')[:1]
    except:
        raise Http404('Article not found.')

    return render(request, 'articles/single.html',{'article': a,} )