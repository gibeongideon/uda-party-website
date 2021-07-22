from django import forms
from .models import Checkout
from paypal.pro.forms import PaymentForm



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = (
            # "user",
            # "email",
            "amount",
        )


# class PayPalmentForm(PaymentForm):
#     class Meta:
#         # model = Checkout
#         fields = (
#             "acct",
#             "cvv2",
#         )
