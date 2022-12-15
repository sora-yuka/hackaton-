from django.core.mail import send_mail
    
def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'User activation',
        full_link,
        'sabyrkulov.nurmuhammed@gmail.com',
        [email],
    )

def send_confirmation_code(email, code):
    send_mail(
        'Password recovery',
        f'Here it is: {code}',
        'sabyrkulov.nurmuhammed@gmail.com',
        [email],
    )