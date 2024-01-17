from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile_update/',views.UserAccountUpdateView.as_view(),name='profile_update'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    path('donate/update/<int:pk>/', views.BookDonateUpdateView.as_view(), name='update_donate_book'),
    path('', views.UserLogoutView.as_view(), name='user_logout'),
    path('active/<str:uid64>/<str:token>/',views.activate, name='activate'),
    path('redeem/<int:gift_id>/', views.RedeemGiftView.as_view(), name='redeem_gift'),
]