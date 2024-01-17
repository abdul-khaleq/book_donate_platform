from django.contrib import admin
from .models import UserAccount, RedeemHistory

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(RedeemHistory)