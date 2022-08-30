#the purpose of view.py is to handle http request
from django.shortcuts import render
from wallet.models import Wallet
from .forms import CustomerRegistrationForm
#learn more on what is contained inside http request
def register_customer(request):
    form = CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {"form":form})
    

