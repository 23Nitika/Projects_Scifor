from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def members(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'full_name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        email_message = f"""
        New Message: {data['message']}
        
        From: {data['email']}
        """

        send_mail(data['subject'], email_message, '', ['nitikagoyal178@gmail.com'])
        
    return render(request, 'email_template.html', {})

