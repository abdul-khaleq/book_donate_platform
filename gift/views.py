from django.shortcuts import render
from django.views import View
from .models import Gift
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class GiftRedeemView(View):
    template_name = 'redeem_gift.html'

    def get(self, request, *args, **kwargs):
        gifts = Gift.objects.all()
        return render(request, self.template_name, {'gifts': gifts})
