from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test Email from Django'
    message = 'Hello! This is a test email sent from Django using Gmail.'
    from_email = 'hishu295@gmail.com'  # replace with your Gmail
    recipient_list = ['theharsh025@gmail.com']  # replace with recipient

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")
