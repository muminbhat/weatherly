from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/contact', views.contact, name='contact'),
    path('pages/about', views.about, name='about')
]