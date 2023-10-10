from django.shortcuts import render , HttpResponse , get_list_or_404 , get_object_or_404 , redirect
from .forms import MessageSenderForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage  
from .models import Message
from .utils import send_verification_email
from .tokens import account_activation_token
from .serializers import MessageSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
# Create your views here.


def home(request):
    title = 'خانه'
    if request.method == "POST":
        form = MessageSenderForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            message = request.POST['message']
            new_message = Message.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                message = message
            )
            new_message.save()
                   
            mail_subject = 'تایید ایمیل'
            page_template_url = 'accounts/emails/email_verification.html'
            send_verification_email(request , new_message ,mail_subject , page_template_url)
          
        else:
            return HttpResponse("Failed")
            

    form = MessageSenderForm()
    context = {
        'title' : title,
        'form' : form
    }
    return render(request , 'main/home.html' , context)



def email_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        message = Message.objects.get(pk=uid)
    except(TypeError , ValueError , OverflowError , message.DoesNotExist):
        message = None
    if message is not None and account_activation_token.check_token(message , token):
        message.activate = True
        message.save()
        messages.success(request , 'با موفقیت تایید شدید')
        return redirect("main:home")
    else:
        messages.error(request , ' تایید ایمیل با مشکل مواجه شد ')
        return redirect("main:home")
    

    # API VIEWS


@api_view(['GET'])
def messageListApi(request : Request):
    messages = Message.objects.all()
    message_serializer = MessageSerializers(messages  ,many=True)
    return Response(message_serializer.data , status.HTTP_200_OK)



