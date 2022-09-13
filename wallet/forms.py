# importing the library called forms
from dataclasses import field, fields
from django import forms
from .models import Account, Customer, Receipt
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import Currency
from .models import Thirdparty
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward
from django.forms import ModelForm

#creating a class to represent the form we want to create 
class CustomerRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Customer
        fields=('first_name','last_name',"address","phone_number","email", "gender", "age", "password", "id_number","nationality")
        widgets={
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "last_name":forms.TextInput(attrs={'class':"form-control"}),
            "address":forms.TextInput(attrs={'class':"form-control"}),
            "phone_number":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),
            "gender":forms.TextInput(attrs={'class':"form-control"}),
            "age":forms.TextInput(attrs={'class':"form-control"}),
            "password":forms.TextInput(attrs={'class':"form-control"}),
            "id_number":forms.TextInput(attrs={'class':"form-control"}),
            "nationality":forms.TextInput(attrs={'class':"form-control"}),
            # "date_of_registration":forms.TextInput(attrs={'class':"form-control"}),     
        }

#Wallet
class WalletRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Wallet
        fields=('balance','customer','amount','time','status','currency','pin')
        widgets={
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "customer":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "time":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
            "currency":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
        }

#account
class AccountRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Account
        fields=('account_number','account_type','account_balance','account_name','wallet')
        widgets={
            "account_number":forms.TextInput(attrs={'class':"form-control"}),
            "account_type":forms.TextInput(attrs={'class':"form-control"}),
            "account_balance":forms.TextInput(attrs={'class':"form-control"}),
            "account_name":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
        }

#transaction
class TransactionRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Transaction
        fields=('transaction_amount','transaction_number','transaction_type','transaction_charge','date_and_time','destination_account','reciept','wallet','origin_account')
        widgets={
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_number":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_type":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_charge":forms.TextInput(attrs={'class':"form-control"}),
            "date_and_time":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "reciept":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "origin_account":forms.TextInput(attrs={'class':"form-control"}),
        }
        

#cards
class CardRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Card
        fields=('card_number','card_name','date_issued','card_type','expiry_date','security_code','wallet','account','issuer')
        widgets={
            "card_number":forms.TextInput(attrs={'class':"form-control"}),
            "card_name":forms.TextInput(attrs={'class':"form-control"}),
            "date_issued":forms.TextInput(attrs={'class':"form-control"}),
            # "CARD_CHOICES":forms.TextInput(attrs={'class':"form-control"}),
            "card_type":forms.TextInput(attrs={'class':"form-control"}),
            "expiry_date":forms.TextInput(attrs={'class':"form-control"}),
            "security_code":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "account":forms.TextInput(attrs={'class':"form-control"}),
            # "ISSUER_CHOICES":forms.TextInput(attrs={'class':"form-control"}),
            "issuer":forms.TextInput(attrs={'class':"form-control"}),    
        }

#currency
class CurrencyRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Currency
        fields=('country','symbol','amount')
        widgets={
            "country":forms.TextInput(attrs={'class':"form-control"}),
            "symbol":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
        }

#thirdparty
class ThirdpartyRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Thirdparty
        fields=('transaction','name','account_number','location','amount','currency')
        widgets={
            "transaction":forms.TextInput(attrs={'class':"form-control"}),
            "name":forms.TextInput(attrs={'class':"form-control"}),
            "account_number":forms.TextInput(attrs={'class':"form-control"}),
            "location":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "currency":forms.TextInput(attrs={'class':"form-control"}),
        }

#notification
class NotificationRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Notification
        fields=('message','recipient','date_time','status')
        widgets={
            # "MESSAGE_CHOICES":forms.TextInput(attrs={'class':"form-control"}),
            "message":forms.TextInput(attrs={'class':"form-control"}),
            # "title":forms.TextInput(attrs={'class':"form-control"}),
            "recipient":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
            # "STATUS_CHOICES":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
        }

#receipt
class ReceiptRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Receipt
        fields=('receipt_type','date','bill_number','amount','customer','receipt_file')
        widgets={
            "receipt_type":forms.TextInput(attrs={'class':"form-control"}),
            "date":forms.TextInput(attrs={'class':"form-control"}),
            "bill_number":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "customer":forms.TextInput(attrs={'class':"form-control"}),
            "receipt_file":forms.TextInput(attrs={'class':"form-control"}),
        }

#loan
class LoanRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Loan
        fields=('loan_type','amount','interest_rate','wallet','loan_balance','guarantor','payment_due_date')
        widgets={
            "loan_type":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "interest_rate":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "loan_balance":forms.TextInput(attrs={'class':"form-control"}),
            "guarantor":forms.TextInput(attrs={'class':"form-control"}),
            "payment_due_date":forms.TextInput(attrs={'class':"form-control"}),
        } 

#reward
class RewardRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Reward
        fields=('transaction','customer_id','message','date_time','points','recipient') 
        widgets={
            "transaction":forms.TextInput(attrs={'class':"form-control"}),
            "customer_id":forms.TextInput(attrs={'class':"form-control"}),
            "message":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
            "points":forms.TextInput(attrs={'class':"form-control"}),
            "recipient":forms.TextInput(attrs={'class':"form-control"}),
        }          
    
        
        

       

