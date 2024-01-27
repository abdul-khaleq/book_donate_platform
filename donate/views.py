from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from . import forms
from .models import BookDonateModel
from user.models import UserAccount
from django.views.generic import CreateView, DetailView, ListView
from django.conf import settings
from django.core.mail import send_mail

# Create your views here. 
@method_decorator(login_required, name='dispatch')
class BookDonateCreateView(LoginRequiredMixin, CreateView):
    model = BookDonateModel
    form_class = forms.BookDonateForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        user_account = UserAccount.objects.get(user=self.request.user)
        user_account.coins +=10
        user_account.save()
        messages.success(self.request, 'The book has been donated successfully. 10 coins added to your account.')
        subject = 'Thanks for donation to Donate books'
        message = f'Hi {self.request.user.first_name} {self.request.user.last_name}, The book has been donated successfully. 5 coins added to your account.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )
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
    
class BooksListView(ListView):
    model = BookDonateModel
    template_name = 'books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = BookDonateModel
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    context_object_name = 'book'