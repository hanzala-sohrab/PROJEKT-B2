from django.shortcuts import render
from django.http import HttpResponse

import razorpay
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KEY_ID = ''
KEY_SECRET = ''

with open(BASE_DIR + "/SECRETS/rzp_key_id.txt") as f:
    KEY_ID = f.read().strip()

with open(BASE_DIR + "/SECRETS/rzp_key_secret.txt") as f:
    KEY_SECRET = f.read().strip()

client = razorpay.Client(auth=(str(KEY_ID), str(KEY_SECRET)))


def testing(request):
    return render(request, 'order.html', {})


def create_order(request):
    context = {}
    if request.method == 'POST':
        print("INSIDE Create Order!!!")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # products = request.POST.getlist('product')
        # print(products)

        order_amount = 10000
        # if products == ['cb1']:
        #     order_amount = 1000
        # elif products == ['cb2']:
        #     order_amount = 2000
        # elif products == ['cb3']:
        #     order_amount = 5000
        # elif products == ['cb1', 'cb2']:
        #     order_amount = 3000
        # elif products == ['cb1', 'cb3']:
        #     order_amount = 6000
        # elif products == ['cb2', 'cb3']:
        #     order_amount = 7000
        # elif products == ['cb1', 'cb2', 'cb3']:
        #     order_amount = 8000
        # products_list = ['cb1', 'cb2', 'cb3']

        # for product in products:
        #     if product == 'cb1':
        #         order_amount += 1000
        #     elif product == 'cb2':
        #         order_amount += 2000
        #     elif product == 'cb3':
        #         order_amount += 3000
        # order_amount = len(products) * 1000

        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        # order_receipt = 'xyzrandom18553'
        notes = {
            'Shipping address': 'Bommanahalli, Bangalore'
        }

        # CREATING ORDER
        response = client.order.create(
            dict(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0'))
        order_id = response['id']
        order_status = response['status']

        if order_status == 'created':
            # Server data for user convenience
            # context['product_id'] = products
            context['price'] = order_amount
            context['name'] = name
            context['phone'] = phone
            context['email'] = email

            context['id'] = KEY_ID

            # data that'll be send to the razorpay for
            context['order_id'] = order_id

            return render(request, 'confirm_order.html', context)

        # print('\n\n\nresponse: ',response, type(response))
    return HttpResponse('<h1>Error in  create order function</h1>')


def payment_status(request):
    response = request.POST

    params_dict = {
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Failure!!!'})
