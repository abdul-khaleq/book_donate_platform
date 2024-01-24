from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BookDonateCreateView.as_view(), name='donate_book'),
]