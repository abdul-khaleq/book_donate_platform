from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import ContactModel
from .forms import ContactForm

from django.conf import settings
from django.core.mail import send_mail


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'

# class ContactUsCreateView(CreateView):
#     template_name = 'contact_us.html'
#     model = ContactModel
#     form_class = ContactForm
#     success_url = reverse_lazy('homepage')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Your message has been received successfully. Our terms member will contact you very soon')
#         subject = 'Thanks for contacting with Donate books'
#         message = f'Hi {self.request.user.first_name} {self.request.user.last_name}, Your message has been received successfully. Our terms member will contact you very soon.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [self.request.user.email, ]
#         send_mail( subject, message, email_from, recipient_list )

#     def form_invalid(self, form):
#         messages.error(self.request, 'Info incorrect. Please check your input.')
#         return super().form_invalid(form)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type'] = 'Contact Us'
#         context['button_text'] = 'Submit'
#         context['icon'] = 'fa-solid fa-address-card'
#         context['has_account'] = "Return to?"
#         context['redirect'] = "homepage"
#         context['user_to_another'] = "Home"
#         return context
    


class ContactUsCreateView(CreateView):
    template_name = 'contact_us.html'
    model = ContactModel
    form_class = ContactForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your message has been received successfully. Our terms member will contact you very soon')
        subject = 'Thanks for contacting with Donate books'
        message = f'Hi {self.object.name}, Your message has been received successfully. Our terms member will contact you very soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.object.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Info incorrect. Please check your input.')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Contact Us'
        context['button_text'] = 'Submit'
        context['icon'] = 'fa-solid fa-address-card'
        context['has_account'] = "Return to?"
        context['redirect'] = "homepage"
        context['user_to_another'] = "Home"
        return context