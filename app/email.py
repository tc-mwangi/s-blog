# from threading import Thread
# from flask import current_app
# from flask_mail import Message
# from app import mail


# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)


# def send_email(subject, sender, recipients, text_body, html_body):
#     msg = Message(subject, sender=sender, recipients=recipients)
#     msg.body = text_body
#     msg.html = html_body
#     Thread(target=send_async_email,
#            args=(current_app._get_current_object(), msg)).start()

from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'saber.dangermouse@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
