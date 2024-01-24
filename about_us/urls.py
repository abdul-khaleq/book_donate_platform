from django.urls import path
from . import views

urlpatterns = [

    path('', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact_us/', views.ContactUsCreateView.as_view(), name='contact_us'),

]
