from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
# Create your views here.



def index(request):
    context = {}    

    return render(request, 'main/index.html', context)

def about(request):
    context = {}    

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
