from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ContactForm
from .models import Feedback
from apps.article.models import Article
# Create your views here.



def index(request):
    articles = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles, 3)  # Show 3 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': page_obj,
    }    

    return render(request, 'main/index.html', context)

def about(request):
    feedback = Feedback.objects.all()
    context = {
        'object_list': feedback,
    }    

    return render(request, 'main/about.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            reverse_url = reverse('main:contact')
            messages.success(request, 'Your message has been sent successfully!')
            return redirect(reverse_url)
        
    context = {
        'form': form,
    }    

    return render(request, 'main/contact.html', context)
