from django.db import models

# Create your models here.




class Message(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=False , blank=True , null=True)

    class Meta:
        ordering = ['sent']

    def __str__(self):
        return self.email