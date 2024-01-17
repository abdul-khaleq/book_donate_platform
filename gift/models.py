from django.db import models

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='gift/media/images/')
    coins_required = models.IntegerField()
    quantity = models.PositiveBigIntegerField(default=10)
    def __str__(self):
        return str(self.name)