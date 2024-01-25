from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BookDonateCreateView.as_view(), name='donate_book'),
    path('books/', views.BooksListView.as_view(), name='books'),
    path('book_detail/<int:id>', views.BookDetailView.as_view(), name='book_details'),
]