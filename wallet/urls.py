import imp
from django .urls import path

from wallet.models import Notification
from .views import register_account
from .views import register_card
from . import views
from .views import register_currency
from .views import register_customer
from .views import register_loan
from .views import register_notification
from .views import register_wallet
from .views import register_receipt
from .views import register_reward
from .views import register_thirdparty
from .views import register_transaction
from .views import customer_profile
from .views import edit_customer
from .views import wallet_profile
from .views import edit_wallet
from .views import account_profile
from .views import edit_account
from .views import edit_transaction
from .views import transaction_profile
from .views import cards_profile
from .views import edit_cards
from .views import edit_notification
from .views import notification_profile
from .views import loan_profile
from .views import edit_loan
from .views import receipt_profile
from .views import edit_receipt



urlpatterns=[
    path("register/", register_customer, name = "registration"),
    path("customers/", views.list_customers, name="customers_list"),
    path("customer/<int:id>",customer_profile, name="customer_profile"),
    path("customers/edit/<int:id>", edit_customer, name="edit_customer"),
    path("wallet/", register_wallet, name = "registration"), 
    path("wallets/", views.list_wallets, name="wallets_list"),
    path("wallet/<int:id>", wallet_profile, name="wallet_profile"),
    path("wallets/edit/<int:id>", edit_wallet, name="edit_wallet"),
    path("account/", register_account, name = "registration"),
    path("accounts/", views.list_accounts, name="accounts_list"),
    path("account/<int:id>", account_profile, name="account_profile"),
    path("accounts/edit/<int:id>", edit_account, name="edit_account"),
    path("transaction/", register_transaction, name = "registration"),
    path("transactions/", views.list_transactions, name="transactions_list"),
    path("transaction/<int:id>",transaction_profile, name="transaction_profile"),
    path("transactions/edit/<int:id>", edit_transaction, name="edit_transaction"),
    path("card/", register_card, name = "registration"),
    path("cards/", views.list_cards, name="cards_list"),
    path("card/<int:id>",cards_profile, name="cards_profile"),
    path("cards/edit/<int:id>", edit_cards, name="edit_cards"),
    path("currency/", register_currency, name = "registration"),
    path("currencys/", views.list_currencys, name="currencys_list"),
    path("thirdparty/", register_thirdparty, name = "registration"),
    path("thirdpartys/", views.list_thirdpartys, name="thirdpartys_list"),
    path("notification/", register_notification, name = "registration"),
    path("notifications/", views.list_notifications, name="notifications_list"),
    path("notification/<int:id>",notification_profile, name="notification_profile"),
    path("notifications/edit/<int:id>", edit_notification, name="edit_notification"),
    path("receipt/", register_receipt, name = "registration"),
    path("receipts/", views.list_receipts, name="receipts_list"),
    path("receipt/<int:id>",receipt_profile, name="receipt_profile"),
    path("receipts/edit/<int:id>", edit_receipt, name="edit_receipt"),
    path("loan/", register_loan, name = "registration"),
    path("loans/", views.list_loans, name="loans_list"),
    path("loan/<int:id>",loan_profile, name="loan_profile"),
    path("loans/edit/<int:id>", edit_loan, name="edit_loan"),
    path("reward/", register_reward, name = "registration"),
    path("rewards/", views.list_rewards, name="rewards_list"),
]

