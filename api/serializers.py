from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Transaction
from wallet.models import Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "address", "phone_number")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("balance", "amount", "status", "currency") 

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_number", "account_type", "account_balance", "account_name") 

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_number", "card_name", "date_issued", "card_type")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("reciept", "destination_account", "transaction_type", "transaction_number")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_type", "amount", "loan_balance", "guarantor")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("receipt_type", "bill_number", "amount", "customer")  

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("message", "status", "date_time", "recipient") 