from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token  
def send_verification_email(request , new_message  ,mail_subject , page_template_url):
    current_site = get_current_site(request)  
    message = render_to_string(page_template_url, {  
                'new_message': new_message,
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(new_message.pk)),  
                'token':account_activation_token.make_token(new_message),  
            })  
    to_email = new_message.email 
    email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
    email.send()  