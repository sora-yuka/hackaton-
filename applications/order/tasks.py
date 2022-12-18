from django.core.mail import send_mail
from main.celery import app

@app.task
def send_confirm_link_celery(email, confirm_code):
    full_link = f"http://localhost:8000/shop/order/activate/{confirm_code}"
    send_mail(
        "Order confirmation link",
        f"Here is your link: {full_link}",
        "sabyrkulov.nurmuhammed@gmail.com",
        [email]
    )