from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment, Tags, Author, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def article_list(request):
    page = request.GET.get('page')
    tag = request.GET.get('tag')
    category = request.GET.get('category')
    article = Article.objects.all()

    paginator = Paginator(article, 2)  # 3 ta maqola har sahifada
    try:
        page_objects = paginator.get_page(page)
    except PageNotAnInteger:
        page_objects = paginator.get_page(1)
    except EmptyPage:
        page_objects = paginator.get_page(paginator.num_pages)
    


    if tag:
        article = article.filter(tags__name=tag)

    if category:
        article = article.filter(category__name=category)

    context = {
        'articles': page_objects,
    }


    return render(request, 'article/blog.html', context)



def article_detail(request, slug):

    article = get_object_or_404(Article, slug=slug)
    author = Author.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()

    comments = Comment.objects.filter(article.id=article.id)

    context = {
        'article': article,
        'author': author,
        'category': category,
        'tags': tags
    }


    return render(request, 'article/blog-single.html', context)

