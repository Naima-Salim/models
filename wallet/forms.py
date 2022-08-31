# importing the library called forms
from dataclasses import field, fields
import imp
from pyexpat import model
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
        fields="__all__"

#Wallet
class WalletRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Wallet
        fields="__all__"

#account
class AccountRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Account
        fields="__all__"

#transaction
class TransactionRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Transaction
        fields="__all__"

#cards
class CardRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Card
        fields="__all__"

#currency
class CurrencyRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Currency
        fields="__all__"

#thirdparty
class ThirdpartyRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Thirdparty
        fields="__all__"

#notification
class NotificationRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Notification
        fields="__all__"

#receipt
class ReceiptRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Receipt
        fields="__all__"

#loan
class LoanRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Loan
        fields="__all__"  

#reward
class RewardRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Reward
        fields="__all__"              
    
        
        

       

