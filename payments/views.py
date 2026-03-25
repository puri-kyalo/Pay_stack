from django.shortcuts import render
from django.conf import settings
from .models import Payment

def checkout_view(request):
    context = {
        'public_key': "pk_test_ed512a6f77ceb8ab0dd5856c42ae95ce8c4015d0", 
    }
    return render(request, 'payments/checkout.html', context)

def payment_success(request):
    # 1. Get the data Paystack sent back in the URL
    ref = request.GET.get('ref')
    email = request.GET.get('email')
    amount = request.GET.get('amount')
    first_name = request.GET.get('first_name')

    # 2. Save it to your Record (Database)
    if ref:
        Payment.objects.create(
            first_name=first_name,
            email=email,
            amount=amount,
            reference=ref,
            status="Success"
        )

    return render(request, 'payments/success.html', {'reference': ref})