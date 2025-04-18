from django.shortcuts import render
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
            # Optionally, redirect to a success page or show a success message
            return render(request, 'main/contact.html')
    context = {
        'form': form,
    }    

    return render(request, 'main/contact.html', context)
