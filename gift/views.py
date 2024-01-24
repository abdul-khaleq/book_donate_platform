from django.shortcuts import render
from django.views import View
from .models import Gift
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(login_required, name='dispatch')
class GiftRedeemView(LoginRequiredMixin, View):
    template_name = 'redeem_gift.html'

    def get(self, request, *args, **kwargs):
        gifts = Gift.objects.all()
        return render(request, self.template_name, {'gifts': gifts})
