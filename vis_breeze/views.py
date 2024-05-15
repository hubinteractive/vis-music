from django.shortcuts import render, redirect
from .forms import MyForm, ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import FileResponse

import os

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html',  context)



def about(request):
    context = {

    }
    return render(request, 'about.html',  context)



def contact(request):
    context = {

    }
    return render(request, 'contact.html',  context)



def success(request):
    context = {

    }
    return render(request, 'success.html',  context)



def lana_janjanin(request):
    context = {

    }
    return render(request, 'lana_janjanin.html',  context)


def jazz_orchestra(request):
    context = {

    }
    return render(request, 'jazz_orchestra.html',  context)


def kafka(request):
    context = {

    }
    return render(request, 'kafka.html',  context)



def vlatko(request):
    context = {

    }
    return render(request, 'vlatko.html',  context)



def dilatum(request):
    context = {

    }
    return render(request, 'dilatum.html',  context)


def matija(request):
    context = {

    }
    return render(request, 'matija.html',  context)


def vasil(request):
    context = {

    }
    return render(request, 'vasil.html',  context)


def programme(request):
    context = {

    }
    return render(request, 'programme.html',  context)


def terms(request):
    context = {

    }
    return render(request, 'terms.html',  context)


def subscribe(request):
    context = {

    }
    return render(request, 'subscribe.html',  context)


def pdf(request):

    file = os.path.join(settings.BASE_DIR, 'static/programme_vis_2024.webp')

    fileOpened = (open, 'rb')

    return FileResponse(fileOpened)


    # context = {

    # }
    # return render(request, 'programme_vis_2024.pdf',  context)






def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            # Access form data using form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return render (request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
   return render (request, 'success.html')




def contact(request):
    form_class = ContactForm
    # fieels = '__all__'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

 
        EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'igor.nikolovski71@outlook.com', # Send from (your website)
               ['igor.nikolovski71@gmail.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

        return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})