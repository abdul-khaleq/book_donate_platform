from django.urls import path
from . import views
from user.views import RedeemGiftView

urlpatterns = [
    path('', views.GiftRedeemView.as_view(), name='gift'),
]