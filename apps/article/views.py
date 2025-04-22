from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment, Tags, Author
# Create your views here.


def article_list(request):
    article = Article.objects.all()

    context = {
        'articles': article,
    }


    return render(request, 'article/blog.html', context)



def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    author = Author.objects.all()
    category = Category.objects.all()

    context = {
        'article': article,
        'author': author,
        'category': category,
    }


    return render(request, 'article/blog-single.html', context)