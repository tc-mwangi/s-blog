from flask import render_template, current_app
from app.email import send_email


def send_welcome_email(user):
    send_email(('[PitchView] Welcome'),
               sender=current_app.config['ADMINS'][0],
               recepients=[user.email],
               text_body=render_template('email/welcome_user.txt',
                                         user=user),
               html_body=render_template('email/welcome_user.html',
                                         user=user))

