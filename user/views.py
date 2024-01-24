from typing import Any
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import  LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import FormView,ListView
from django.contrib.auth.models import User
from .models import Gift,UserAccount, RedeemHistory
from donate.models import BookDonateModel
from donate.forms import BookDonateForm
from django.views.generic import TemplateView

from django.utils.decorators import method_decorator
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
    
class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        user = form.save()
        token = default_token_generator.make_token(user)
        # print("token ", token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        # print("uid ", uid)
        confirm_link = f"https://book-donate-platform-g1fx.onrender.com/user/active/{uid}/{token}"
        # confirm_link = f"http://127.0.0.1:8000/user/active/{uid}/{token}"
        email_subject = "Confirm Your Email"
        email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
        email = EmailMultiAlternatives(email_subject , '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
        # login(self.request, user)
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Registration info incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Sign up'
        context['icon'] = 'fa-regular fa-address-card'
        context['has_account'] = "Already have an account?"
        context['redirect'] = "user_login"
        context['user_to_another'] = "Sign in"
        return context
    
def activate(request, uid64, token):
    print("RequesT",request, "UiD",uid64, "TokeN", token)
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
        print(user)
    except(User.DoesNotExist):
        user = None
        print(user)
    # if user is not None and default_token_generator.check_token(user, token):
    if user is not None:
        print("AMi paichi")
        user.is_active = True
        user.save()
        return redirect('user_login')
    else:
        return redirect('user_register')
    
    
class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in info incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Sign in'
        context['icon'] = 'fa-solid fa-unlock-keyhole'
        context['has_account'] = "Don't you have an account?"
        context['redirect'] = "user_register"
        context['user_to_another'] = "Sign up"
        return context


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})

class UserProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_account = self.request.user.user
        except UserAccount.DoesNotExist:
            user_account = None
        context['user_account'] = user_account
        gifts = RedeemHistory.objects.filter(user=self.request.user)
        books = BookDonateModel.objects.filter(user=self.request.user)
        context['books'] = books
        context['gifts'] = gifts
        return context


class ProfileView(ListView):
    model = BookDonateModel
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        gifts = RedeemHistory.objects.filter(user=request.user)
        books = BookDonateModel.objects.filter(user=self.request.user)
        print(gifts)
        return render(request, self.template_name, {'books':books,'gifts': gifts})


class UserAccountUpdateView(View):
    template_name = 'update_profile.html'

    def get(self, request):
        form = forms.UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully updated')
            return redirect('profile')
        else:
            messages.error(request,'Error updating profile')
        return render(request, self.template_name, {'form': form})
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('user_login')


class BookDonateUpdateView(UpdateView):
    model = BookDonateModel
    form_class = BookDonateForm
    template_name = 'update_donate_book.html'
    success_url = reverse_lazy('profile')


class RedeemGiftView(View):
    def get(self, request, gift_id):
        gift = get_object_or_404(Gift, id=gift_id)
        if request.user.user.coins >= gift.coins_required and gift.quantity > 0:
            request.user.user.coins -= gift.coins_required
            request.user.user.save()
            gift.quantity -= 1
            gift.save()
            RedeemHistory.objects.create(user=request.user, gift=gift)
        return redirect('homepage')
