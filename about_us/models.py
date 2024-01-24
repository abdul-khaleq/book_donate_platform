from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Messaged by: {self.name}"
