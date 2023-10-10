
from django.urls import path , include
from . import views

app_name = 'main'

urlpatterns = [
    path('' , views.home , name='home'),
    path('activate_email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.email_activate, name='email_activate'),


    # API
    path('api/messageList' , views.messageListApi , name='message_list_api')  
]