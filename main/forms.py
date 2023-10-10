from django import forms
from .models import Message


class MessageSenderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Message
        fields = ['first_name' , 'last_name' , 'email' , 'message']
