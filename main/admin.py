from django.contrib import admin
from .models import Message
# Register your models here.



class MessageAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'email' , 'sent' ]




admin.site.register(Message)