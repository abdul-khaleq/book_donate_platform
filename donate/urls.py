from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.BookDonateCreateView.as_view(), name='donate_book'),
    # path('borrow/<int:id>', views.borrowHistory, name='borrow'),
    # path('detail/<int:pk>', views.BookDetailView.as_view(), name='book_details'),
]