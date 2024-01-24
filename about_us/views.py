from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import ContactModel
from .forms import ContactForm

class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

class ContactUsCreateView(CreateView):
    template_name = 'register.html'
    model = ContactModel
    form_class = ContactForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'info incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Contact Us'
        context['icon'] = 'fa-solid fa-address-card'
        context['has_account'] = "Want to login?"
        context['redirect'] = "user_login"
        context['user_to_another'] = "Sign in"
        return context