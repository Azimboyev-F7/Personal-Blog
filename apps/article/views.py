from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment, Tags, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def article_list(request):
    page = request.GET.get('page')
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    article = Article.objects.all()

    paginator = Paginator(article, 3)  # 3 ta maqola har sahifada
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    


    if tag:
        article = article.filter(tags__name=tag)

    if category:
        article = article.filter(category__name=category)

    context = {
        'articles': page,
    }


    return render(request, 'article/blog.html', context)



def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    author = Author.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()

    context = {
        'article': article,
        'author': author,
        'category': category,
        'tags': tags
    }


    return render(request, 'article/blog-single.html', context)

