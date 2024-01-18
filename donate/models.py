from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookDonateModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='donate/media/images/')
    donated_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Book name: {self.title}"
