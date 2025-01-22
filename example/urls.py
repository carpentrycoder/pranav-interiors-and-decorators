# example/urls.py
from django.urls import path

from .views import index,contact,work


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('ourwork/', work, name='work')
]

