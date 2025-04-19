from django.shortcuts import render
from .models import Article, Category, Comment, Tags
# Create your views here.


def article_list(request):
    article = Article.objects.all()

    context = {
        'articles': article,
    }


    return render(request, 'article/blog.html', context)



def article_detail(request, slug):
    article = Article.objects.all(slug=slug)

    context = {
        'article': article,
    }


    return render(request, 'article/blog-single.html', context)