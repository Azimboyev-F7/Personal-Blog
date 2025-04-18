from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=221)
    position = models.CharField(max_length=221)
    message = models.TextField()
    image = models.ImageField(upload_to='feedback/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=221)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name