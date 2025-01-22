# example/views.py
from django.shortcuts import render
from .models import HostedImage

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def contact(request):
    # Your view logic here
    return render(request, 'contactUs.html')

def work(request):
    images = HostedImage.objects.all()  # Fetch all the images
    return render(request, 'showcase.html', {'images': images})