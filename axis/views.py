from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing-page.html')

def the_observer(request):
    return render(request, 'the-observer.html')
