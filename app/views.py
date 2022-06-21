from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        email_address = request.POST['email']
        message = request.POST['message']

        contact = Contact(email_address=email_address, message=message)
        contact.save()

        return redirect('home')