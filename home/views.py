# from __future__ import unicode_literals
from django.views.generic import FormView
from django.views.generic import TemplateView
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from .models import Checkout
from .forms import CheckoutForm
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect, reverse

from django.conf import settings
from .forms import CheckoutForm
from paypal.pro.views import PayPalPro


# paypals

def process_payment(request):
    latest_id = max((obj.id for obj in Checkout.objects.filter(
        user=request.user)))

    amount = Checkout.objects.get(id=latest_id).amount
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': f'{amount}',
        'item_name': f'Topup-{latest_id}-for-{request.user.id}',
        'invoice': f'{latest_id}',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}'.format(host),
        'cancel_return': 'http://{}/donate'.format(host),

        # 'return_url': 'http://{}{}'.format(host,
        #                                    reverse('payment_done')),
        # 'cancel_return': 'http://{}{}'.format(host,
        #                                       reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(
        request,
        'home/paypal/process_payment.html',
        {'amount': amount, 'form': form})


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.user = request.user
            # form.email = request.user.email
            form.save()
            # cleaned_data = form.cleaned_data
            return redirect('/home/paypal/process-payment')
    else:
        form = CheckoutForm()
        return render(request, 'home/donate.html', locals())


@csrf_exempt
def payment_done(request):
    return render(request, 'home/paypal/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'home/paypal/payment_cancelled.html')


