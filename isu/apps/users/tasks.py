from time import sleep
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activate_link(email, message):
        send_mail(
            subject="Verify your email",
            message=message,
            from_email="test@noreply.org",
            recipient_list=[email],
        )

 


