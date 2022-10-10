#the purpose of view.py is to handle http request
from urllib import request
from django.shortcuts import render
from wallet.models import Account, Card, Currency, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
from wallet.models import Customer
from . import forms

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
import wallet
#learn more on what is contained inside http request

#customer
def register_customer(request):
    if request.method =="POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
        {"form":form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request, "wallet/customers_list.html",
    {"customers":customers})

def customer_profile(request,id):
    customer = models.Customer.objects.get(id = id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_customer(request,id):
    customer = models.Customer.objects.get(id=id)
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST,instance=customer)

    if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form =forms.CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer.html",{"form":form})
       
#Wallet
def register_wallet(request):
    if request.method =="POST":
      form = WalletRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
    else:
        form=WalletRegistrationForm    
    return render (request,"wallet/register_wallet.html",
    {"form":form}) 

def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request, "wallet/wallets_list.html",
    {"wallets":wallets})    

def wallet_profile(request,id):
    wallet = models.Wallet.objects.get(id = id)
    return render(request,"wallet/wallet_profile.html",{"wallet":wallet})

def edit_wallet(request,id):
    wallet = models.Wallet.objects.get(id=id)
    if request.method == "POST":
        form = forms.WalletRegistrationForm(request.POST,instance=wallet)

    if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form =forms.WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/edit_wallet.html",{"form":form})

#account
def register_account(request):
    if request.method =="POST":
     form = AccountRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=AccountRegistrationForm    
    return render (request,"wallet/register_account.html",
    {"form":form}) 

def list_accounts(request):
    accounts=Account.objects.all()
    return render(request, "wallet/accounts_list.html",
    {"accounts":accounts})     

def account_profile(request,id):
    account = models.Wallet.objects.get(id = id)
    return render(request,"wallet/account_profile.html",{"account":account})

def edit_account(request,id):
    account = models.Account.objects.get(id=id)
    if request.method == "POST":
        form = forms.AccountRegistrationForm(request.POST,instance=account)

    if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form =forms.AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_account.html",{"form":form})

#transaction
def register_transaction(request):
    if request.method =="POST":
     form = TransactionRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=TransactionRegistrationForm()
    return render (request,"wallet/register_transaction.html",
    {"form":form}) 

def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request, "wallet/transactions_list.html",
    {"transactions":transactions}) 

def transaction_profile(request,id):
    transaction = models.Transaction.objects.get(id = id)
    return render(request,"wallet/transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id):
    transaction = models.Transaction.objects.get(id=id)
    if request.method == "POST":
        form = forms.TransactionRegistrationForm(request.POST,instance=transaction)

    if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
        form =forms.TransactionRegistrationForm(instance=transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})

#cards
def register_card(request):
    if request.method =="POST":   
     form = CardRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=CardRegistrationForm    
    return render (request,"wallet/register_card.html",
    {"form":form})

def list_cards(request):
    cards=Card.objects.all()
    return render(request, "wallet/cards_list.html",
    {"cards":cards}) 

def cards_profile(request,id):
    cards = models.Cards.objects.get(id = id)
    return render(request,"wallet/cards_profile.html",{"cards":cards})

def edit_cards(request,id):
    cards = models.Cards.objects.get(id=id)
    if request.method == "POST":
        form = forms.CardRegistrationForm(request.POST,instance=cards)

    if form.is_valid():
            form.save()
            return redirect("cards_profile",id=cards.id)
    else:
        form =forms.CardRegistrationForm(instance=cards)
        return render(request,"wallet/edit_cards.html",{"form":form})

#currency
def register_currency(request):
    if request.method =="POST":
     form = CurrencyRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=CurrencyRegistrationForm        
    return render (request,"wallet/register_currency.html",
    {"form":form})

def list_currencys(request):
    currencys=Currency.objects.all()
    return render(request, "wallet/currencys_list.html",
    {"currencys":currencys})     

#thirdparty
def register_thirdparty(request):
    if request.method =="POST":
     form = ThirdpartyRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=ThirdpartyRegistrationForm    
    return render (request,"wallet/register_thirdparty.html",
    {"form":form})  

def list_thirdpartys(request):
    thirdpartys=Thirdparty.objects.all()
    return render(request, "wallet/thirdpartys_list.html",
    {"thirdpartys":thirdpartys})     

#notification
def register_notification(request):
    if request.method =="POST":
     form = NotificationRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=NotificationRegistrationForm    
    return render (request,"wallet/register_notification.html",
    {"form":form}) 

def list_notifications(request):
    notifications=Notification.objects.all()
    return render(request, "wallet/notifications_list.html",
    {"notifications":notifications})    

def notification_profile(request,id):
    notification = models.Notification.objects.get(id = id)
    return render(request,"wallet/notification_profile.html",{"notification":notification})

def edit_notification(request,id):
    notification = models. Notification.objects.get(id=id)
    if request.method == "POST":
        form = forms.NotificationRegistrationForm(request.POST,instance=notification)

    if form.is_valid():
            form.save()
            return redirect("notifiction_profile",id=notification.id)
    else:
        form =forms.NotificationRegistrationForm(instance=cards)
        return render(request,"wallet/edit_notification.html",{"form":form})    

#receipt
def register_receipt(request):
    if request.method =="POST":
     form = ReceiptRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=ReceiptRegistrationForm    
    return render (request,"wallet/register_receipt.html",
    {"form":form}) 

def list_receipts(request):
    receipts=Receipt.objects.all()
    return render(request, "wallet/receipts_list.html",
    {"receipts":receipts})     

def receipt_profile(request,id):
    receipt = models.Receipt.objects.get(id = id)
    return render(request,"wallet/receipt_profile.html",{"receipt":receipt})

def edit_receipt(request,id):
    receipt = models.Receipt.objects.get(id=id)
    if request.method == "POST":
        form = forms.ReceiptRegistrationForm(request.POST,instance=receipt)

    if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)
    else:
        form =forms.ReceiptRegistrationForm(instance=receipt)
        return render(request,"wallet/edit_receipt.html",{"form":form})

#loan
def register_loan(request):
    if request.method =="POST":
     form = LoanRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=LoanRegistrationForm    
    return render (request,"wallet/register_loan.html",
    {"form":form}) 

def list_loans(request):
    loans=Loan.objects.all()
    return render(request, "wallet/loans_list.html",
    {"loans":loans}) 

def loan_profile(request,id):
    loan = models.Loan.objects.get(id = id)
    return render(request,"wallet/loan_profile.html",{"loan":loan})

def edit_loan(request,id):
    loan = models. Loan.objects.get(id=id)
    if request.method == "POST":
        form = forms.LoanRegistrationForm(request.POST,instance=loan)

    if form.is_valid():
            form.save()
            return redirect("loan_profile",id=loan.id)
    else:
        form =forms.LoanRegistrationForm(instance=loan)
        return render(request,"wallet/edit_loan.html",{"form":form}) 

#reward
def register_reward(request):
    if request.method =="POST":
     form = RewardRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=RewardRegistrationForm    
    return render (request,"wallet/register_reward.html",
    {"form":form}) 

def list_rewards(request):
    rewards=Reward.objects.all()
    return render(request, "wallet/rewards_list.html",
    {"rewards":rewards})    