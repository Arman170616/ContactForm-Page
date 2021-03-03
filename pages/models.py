from django.db import models

# Create your models here.

class ContactPage(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    attachment = models.FileField(upload_to='media/file/', null=True, blank=True)
    image = models.ImageField(upload_to='media/file/', null = True, blank = True)

    def __str__(self):
        return self.name

    
