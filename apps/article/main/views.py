from django.shortcuts import render

# Create your views here.



def index(request):
    context = {}    

    return render(request, 'article/index.html', context)

def about(request):
    context = {}    

    return render(request, 'article/about.html', context)

def contact(request):
    context = {}    

    return render(request, 'article/contact.html', context)
