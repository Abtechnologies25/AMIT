from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def business_page(request):
    return render(request, 'business.html')

def projects_page(request):
    return render(request, 'projects.html')

def products_page(request):
    return render(request, 'products.html')

def training_page(request):
    return render(request, 'training.html')

def contact_page(request):
    return render(request, 'contactus.html')


def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if subject and name and phone and email and message:
            try:
                email_body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"
                send_mail(subject,email_body, settings.EMAIL_HOST_USER, ['dhilaharis11.abt@gmail.com','dhilaharis.abt@gmail.com'])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "contactus.html", context)