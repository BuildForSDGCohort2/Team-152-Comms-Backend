
# dispatchers.py contain functions and classes that handles actual
# forwarding of communication via specified platforms
# this script could also contain connectors to other libraries
# or modules, should organization require siloed scripts

from smtplib import SMTPAuthenticationError

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.exceptions import TemplateDoesNotExist

from rest_framework.exceptions import APIException
from rest_framework.response import Response


class InvalidTemplate(APIException):
    status_code = 500
    default_detail = 'Template does not exist.'
    default_code = 'invalid_template'

class EmailServerError(APIException):
    status_code = 500
    default_detail = 'Error connecting to SMTP Server'
    default_code = 'smtp_error'


def send_email(template_name, context):
    # i had thought to use an http connector instead
    # to actual endpoints in this same project: email app or sms app
    # but that will not be done for now.
    # i still need to make this function asynchronous though

    """
    Load email template, compile with given context, send using Django's
    email module.
    """

    try:
        html_message = render_to_string(f'{template_name}.txt', context=context)
    except TemplateDoesNotExist:
        raise InvalidTemplate
    
    plain_message = strip_tags(html_message)
    try:
        response_value = send_mail(
            'SkillCafe Communication', # subject
            plain_message, # message
            'SkillCafe Communication <paperboycs30@gmail.com>', # from email
            [ # to emails
                context['to']
            ],
            # html_message=html_message
            )
        print(response_value, type(response_value))
        if response_value == 1:
            return Response(
                {
                    'detail': 'Communication (email) sent successfully.'
                }
            )
        else:
            return Response(
                {
                    'detail': 'Communication might have failed.'
                }
            )
    except SMTPAuthenticationError:
        raise EmailServerError
    # except:
    #     raise
