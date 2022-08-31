#the purpose of view.py is to handle http request
from django.shortcuts import render
from wallet.models import Wallet
from .forms import WalletRegistrationForm
from .forms import CustomerRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm
#learn more on what is contained inside http request

#customer
def register_customer(request):
    form = CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {"form":form})

#Wallet
def register_wallet(request):
    form = WalletRegistrationForm()
    return render (request,"wallet/register_wallet.html",
    {"form":form}) 

#account
def register_account(request):
    form = AccountRegistrationForm()
    return render (request,"wallet/register_account.html",
    {"form":form}) 

#transaction
def register_transaction(request):
    form = TransactionRegistrationForm()
    return render (request,"wallet/register_transaction.html",
    {"form":form}) 

#cards
def register_card(request):
    form = CardRegistrationForm()
    return render (request,"wallet/register_card.html",
    {"form":form}) 

#currency
def register_currency(request):
    form = CurrencyRegistrationForm()
    return render (request,"wallet/register_currency.html",
    {"form":form}) 

#thirdparty
def register_thirdparty(request):
    form = ThirdpartyRegistrationForm()
    return render (request,"wallet/register_thirdparty.html",
    {"form":form})     

#notification
def register_notification(request):
    form = NotificationRegistrationForm()
    return render (request,"wallet/register_notification.html",
    {"form":form}) 

#receipt
def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render (request,"wallet/register_receipt.html",
    {"form":form}) 

#loan
def register_loan(request):
    form = LoanRegistrationForm()
    return render (request,"wallet/register_loan.html",
    {"form":form}) 

#reward
def register_reward(request):
    form = RewardRegistrationForm()
    return render (request,"wallet/register_reward.html",
    {"form":form})     