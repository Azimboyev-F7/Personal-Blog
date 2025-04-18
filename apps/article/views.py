from django.shortcuts import render

# Create your views here.


def article_list(request):

    context = {}


    return render(request, 'article/blog.html', context)



def article_detail(request):

    context = {}


    return render(request, 'article/blog-single.html', context)