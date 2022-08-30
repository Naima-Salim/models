# importing the library called forms
from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Customer
from django.forms import ModelForm
#creating a class to represent the form we want to create 
class CustomerRegistrationForm(ModelForm): #creating a meta class
    class Meta:
        model=Customer
        fields="__all__"