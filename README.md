Project Name: Paystack

Description: A professional Django-based payment integration for GmaX Creatives, featuring a modern split-screen checkout interface specifically optimized for Kenyan Shilling (KES) transactions via M-PESA, Airtel Money, and Card payments.

Key Features

Split-Screen UI: A custom-designed checkout page with a dedicated branding/service summary section and a clean functional form.

Paystack v2 Integration: Utilizes the latest Paystack Inline JS library for a modern, responsive payment popup.

M-PESA Optimization: Specifically configured for the Kenyan market with automatic KES to Cents conversion and mobile money metadata.

Automated Record Keeping: Seamlessly captures and saves transaction details (Name, Email, Amount, and Reference) to a local SQLite database upon successful completion.

Dynamic URL Parameters: Uses modern JavaScript (URLSearchParams) to pass data securely from the frontend to the backend success view.

Responsive Design: Fully styled with custom CSS to ensure a professional experience across desktop and mobile devices.

Technologies Used

Backend: Django 5.0+ (Python 3.12)

Frontend: HTML5, CSS3, JavaScript (ES6+)

Payment Gateway: Paystack API (v2 Inline)

Database: SQLite

Installation Requirements

Python 3.10 or higher

Pip (Python package manager)

Virtual Environment (recommended)

A registered Paystack account to obtain API keys

1. Project Title and Description
Paystack M-PESA Payments in Django
This project serves as a bridge between a Django-based service website and the Paystack payment gateway. It is designed for service providers, like GmaX Creatives, who need a reliable way to collect branding or design fees while maintaining a professional digital record of every transaction.

2. Installation Instructions
   
Clone the repository:

Bash
git clone <your-repository-url>
cd paystack
Create and activate a virtual environment:

Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Apply database migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Create an admin user:

Bash
python manage.py createsuperuser
Start the server:

Bash
python manage.py runserver

3. Basic Usage Examples
Accessing the Checkout: Navigate to http://127.0.0.1:8000/ to view the checkout form.

Processing a Payment: Fill in your name, email, and amount (e.g., 1000). Click "Pay Now" to trigger the M-PESA popup.

Viewing Records: Log in to http://127.0.0.1:8000/admin/ to see the "Payments" table populated with successful transaction data.

4. Features Overview
The system workflow begins at the Checkout View, where user data is collected. The JavaScript Layer then interfaces with Paystack to handle the sensitive payment data. On Success, the user is redirected to a dynamic Success View that extracts URL parameters to create a persistent record in the Payment Model.

5. Configuration Options
   
To configure your API keys, update the checkout_view in payments/views.py:

public_key: Set this to your Paystack Test Public Key (starts with pk_test_).

For production:

Update DEBUG = False in settings.py.

Swap the Test Key for your Live Public Key.

6. Troubleshooting Section
   
Invalid Key Error: Ensure the public key is wrapped in single quotes and is correctly passed to the template.

TemplateDoesNotExist: Confirm that your directory structure follows payments/templates/payments/checkout.html.

CSS Not Loading: If changes aren't appearing, use a hard refresh (Ctrl + F5) to bypass browser caching.

Database Errors: If fields are missing, re-run makemigrations and migrate to update the SQLite schema.

7. Contributing Guidelines
   
Contributions are welcome. Please follow these steps:

Fork the Project.

Create your Feature Branch (git checkout -b feature/NewFeature).

Commit your changes (git commit -m 'Add some NewFeature').

Push to the Branch (git push origin feature/NewFeature).

Open a Pull Request.

8. License Information
Distributed under the MIT License. See LICENSE for more information.

Code Structure Overview
Plaintext
paystack/
├── manage.py
├── payments/
│   ├── admin.py          # Admin interface configuration for Payment records
│   ├── models.py         # Database schema for storing transactions
│   ├── views.py          # Logic for checkout and success redirection
│   ├── static/
│   │   └── payments/
│   │       └── style.css # Custom split-screen styling
│   └── templates/
│       └── payments/
│           ├── checkout.html # Main form and Paystack JS integration
│           └── success.html  # Dynamic receipt and success message
├── core/
│   ├── settings.py       # Project configuration and installed apps
│   └── urls.py           # Global URL routing
└── requirements.txt      # List of project dependencies

