from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from . import forms
from . import models
from user.models import UserAccount
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views import View

# Create your views here. 
@method_decorator(login_required, name='dispatch')
class BookDonateCreateView(LoginRequiredMixin, CreateView):
    model = models.BookDonateModel
    form_class = forms.BookDonateForm
    template_name = 'register.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        user_account = UserAccount.objects.get(user=self.request.user)
        user_account.coins +=10
        user_account.save()
        messages.success(self.request, 'The book has been donated successfully. 5 coins added to your account.')
        return response
    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Donate'
        context['button_text'] = 'Donate'
        context['icon'] = 'fa-solid fa-hand-holding-medical text-info'
        context['has_account'] = "Return"
        context['redirect'] = "homepage"
        context['user_to_another'] = "home"
        return context