from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from . import forms
from . import models
from user.models import UserAccount
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views import View

# Create your views here. 
class BookDonateCreateView(CreateView):
    model = models.BookDonateModel
    form_class = forms.BookDonateForm
    template_name = 'donate_book.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # messages.success(self.request, 'The book has been donated successfully')
        response = super().form_valid(form)
        user_account = UserAccount.objects.get(user=self.request.user)
        user_account.coins +=10
        user_account.save()
        messages.success(self.request, 'The book has been donated successfully. 5 coins added to your account.')
        return response

    def form_invalid(self, form):
        return super().form_invalid(form)
