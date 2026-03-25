Paystack M-PESA Payments in Django
A professional, split-screen checkout integration for GmaX Creatives using the Paystack API. This project demonstrates how to handle Kenyan Shilling (KES) transactions specifically optimized for M-PESA, Airtel Money, and Card payments within a Django environment.

Features Overview
Custom Split UI: A modern, responsive design with a branding/summary section on the left and a payment form on the right.

Dynamic M-PESA Integration: Uses Paystack's latest v2 popup for seamless mobile money prompts.

Real-time Record Keeping: Automatically saves transaction details (Name, Email, Reference, Amount) to a Django SQLite database upon successful payment.

Dynamic Pricing: Users can enter their own amount, which is correctly converted to cents for Paystack processing.

Professional Footer: Integrated high-quality payment logos for M-PESA, Visa, Mastercard, and Airtel.

Technologies Used
Backend: Django 5.0+ (Python 3.12)

Frontend: HTML5, CSS3 (Flexbox), JavaScript (ES6)

Payment Gateway: Paystack Inline JS (v2)

Database: SQLite (default Django)

Installation Requirements
Before you begin, ensure you have the following installed:

Python 3.10 or higher

Pip (Python package manager)

A Paystack account (for API keys)

Setup Instructions
Clone the project and navigate to the directory:

Bash
cd paystack_project
Create and activate a virtual environment:

Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install Django:

Bash
pip install django
Run Migrations to set up the Payment records:

Bash
python manage.py makemigrations
python manage.py migrate
Create a Superuser to view records:

Bash
python manage.py createsuperuser
Configuration
Open payments/views.py and add your Test Public Key from your Paystack Dashboard:

Python
# payments/views.py
def checkout_view(request):
    context = {
        'public_key': 'pk_test_ed512a6f77ceb8ab0dd5856c42ae95ce8c4015d0', 
    }
    return render(request, 'payments/checkout.html', context)
Code Structure Overview
payments/models.py: Defines the Payment class for database records.

payments/views.py: Logic for the checkout page and the success redirection.

payments/templates/payments/checkout.html: The main UI and Paystack JS logic.

payments/static/payments/style.css: All styling, including the "split-screen" layout and branding.

payments/admin.py: Configuration to view transaction history in the Django Admin panel.

Basic Usage Example
To start a transaction:

Navigate to http://127.0.0.1:8000/.

Enter your Name, Email, and the KES Amount.

Click Pay Now.

The Paystack popup will appear; select M-PESA and click Authorize/Success (in test mode).

Troubleshooting
"Please enter a valid Key": Ensure your Public Key in views.py starts with pk_test_ and is wrapped in single quotes.

TemplateDoesNotExist: Ensure your checkout.html is in payments/templates/payments/ (check for the double "payments" folder).

CSS not updating: Use Ctrl + F5 to force the browser to clear the cache and load the latest style.css.

ImportError (django.db): Ensure you use from django.db import models (not import db).

Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.
