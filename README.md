# PROJEKT-B2

**Razorpay**: https://razorpay.com/docs/payment-gateway/web-integration/standard

**Step 1**: Create an Order from your Server
```sh
curl -u "rzp_test_WzfGn5FQwd8woZ":"fKTNimdLaYMJuBmEkeiIjdeR"  -X POST https://api.razorpay.com/v1/orders -H 'content-type:application/json' -d '{    "amount": 50000,    "currency": "INR",    "receipt": "rcptid_11"}'
```

**Step 2**:Pass Order Id and Other Options to the Checkout. Use `payment.html` for this.

**Step 3**: Handle Payment Success and Failure.
