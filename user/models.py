from django.db import models
from django.contrib.auth.models import User
from gift.models import Gift

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    coins= models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

class RedeemHistory(models.Model):
    user = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, related_name='gift', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.gift)
    
