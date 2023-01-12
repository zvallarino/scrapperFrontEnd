from django.db import models

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=50)
    message_time = models.DateField( auto_now=False, auto_now_add=False)
    message = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.username} sent a message that said {self.message} on {self.message_time}'
    