from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('About Success!')

def contact(request):
    return HttpResponse('Contact Success!')