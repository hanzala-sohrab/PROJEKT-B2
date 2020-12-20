# PROJEKT-B2

## Tech-stack:
- Django
- HTML
- CSS
- JavaScript
- Razorpay API

## Steps to run the site locally

**STEP 1** : `git clone https://github.com/hanzala-sohrab/PROJEKT-B2.git`

**STEP 2** : `pip install -r requirements.txt`

**STEP 3** : Go to `main/settings.py` and provide a `SECRET KEY`

**STEP 4** : Go to `payments/view.py` and provide your Razorpay `KEY_ID` and `KEY_SECRET`

**STEP 5** : `python manage.py makemigrations`

**STEP 6** : `python manage.py migrate`

**STEP 7** : Create a superuser using `python manage.py createsuperuser`

**STEP 8** : Run using `python manage.py runserver`

**STEP 9** : In a browser, type in this URL - `127.0.0.1:8000/payments/`
