from django.core.mail import send_mail
from decouple import config
def sendEmail(data):
    return send_mail(
        data['subject'],
        data['body'],
        "sumanaryal83p2@gmail.com",
        ["saagrsaaml@gmail.com"],
        fail_silently=False,
    )