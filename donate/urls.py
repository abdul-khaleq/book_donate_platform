from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.BookDonateCreateView.as_view(), name='donate_book'),
]