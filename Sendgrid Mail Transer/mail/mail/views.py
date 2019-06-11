from django.conf import settings
from django.core.mail import send_mail
#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    subject = 'Trial Message'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = ['']
    contact_message = 'Hey! It works. SendGrid workds!'

    send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
    return HttpResponse('Check Your Mail! ' + to_email[0])
