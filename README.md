# Account-Transfer Project

## Overview
The Account-Transfer project is a Django-based web application designed to manage and transfer funds between accounts. The application includes functionality for listing accounts, viewing account details, importing accounts from a CSV file, and transferring funds between accounts.

## Project Structure

```plaintext
Account-Transfer/
├── accounts/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── accounts/
│   │       ├── account_detail.html
│   │       ├── import_accounts.html
│   │       ├── list_accounts.html
│   │       └── transfer_funds.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── accounts.csv
├── Project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── db.sqlite3
```

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Account-Transfer.git
    cd Account-Transfer
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### Accessing the Application

Once the development server is running, you can access the application at `http://127.0.0.1:8000/`.

### Features

#### Account List

View a list of all accounts:
- Navigate to the home page at `/` to see the list of accounts.
- Each account ID is a link that leads to the account detail page.

#### Account Detail

View details of a specific account:
- Click on an account ID from the account list to view its details, including ID, name, and balance.

#### Import Accounts

Import accounts from a CSV file:
- Navigate to `/import/`.
- Upload a CSV file containing account details (`ID`, `Name`, `Balance`).

#### Transfer Funds

Transfer funds between accounts:
- Navigate to `/transfer/`.
- Fill out the form to transfer funds from one account to another.

### Admin Interface

The admin interface allows for managing accounts and transactions:
- Access the admin interface at `/admin/`.
- Use the admin credentials to log in and manage accounts and transactions.

## Testing

The project includes tests to ensure functionality:
- To run tests, use the command:
    ```bash
    python manage.py test
    ```

## Project Structure Details

### Templates

- `account_detail.html`: Displays the details of a specific account.
- `import_accounts.html`: Provides a form for uploading a CSV file to import accounts.
- `list_accounts.html`: Displays a list of all accounts with options to import accounts and transfer funds.
- `transfer_funds.html`: Provides a form for transferring funds between accounts.

### Models

- `Account`: Represents a bank account with fields for ID, name, and balance.
- `Transaction`: Represents a transaction between two accounts with fields for from_account, to_account, amount, and timestamp.

### Forms

- `TransferForm`: Form for transferring funds between accounts.

### Views

- `AccountListView`: View for listing all accounts.
- `AccountDetailView`: View for displaying account details.
- `TransferFundsView`: View for handling fund transfers between accounts.
- `AccountImportView`: View for handling the import of accounts from a CSV file.

## Asking

This README provides a comprehensive guide to the Account-Transfer project, detailing its structure, installation, usage, and other relevant information. For any further assistance, please refer to the project documentation or contact the project maintainers.