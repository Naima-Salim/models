
from lzma import MODE_FAST
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    address = models.TextField()
    Phone_number=models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    password=models.CharField(max_length=20)
    id_number=models.IntegerField()
    nationality=models.CharField(max_length=20)
    date_of_registration=models.DateTimeField()
    profile_picture=models.FileField()

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey('customer',on_delete=models.CASCADE,related_name='Wallet_customer')
    amount = models.IntegerField()
    time = models.DateTimeField()
    status = models.CharField(max_length=20)
    currency = models.ForeignKey('currency',on_delete=models.CASCADE,related_name='Wallet_currency')
    pin = models.IntegerField()

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    account_name = models.CharField(max_length=20)
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Account_wallet')
    account = models.ForeignKey('account',on_delete=models.CASCADE,related_name='Account_account')

class Transaction(models.Model):
    transaction_ref = models.CharField(max_length=20)
    wallet = models.ForeignKey('wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount = models.IntegerField()
    transaction_number = models.CharField(max_length=20)
    transaction_name = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=20)
    transaction_charge = models.IntegerField()
    date_and_time = models.DateTimeField()
    destination_account = models.ManyToManyRel(Customer,on_delete=models.CASCADE,related_name='Transaction_ destination_account')
    receipt = models.OneToOneRel(Customer,on_delete=models.CASCADE,related_name='Transaction_receipt')
    recipient = models.ForeignKey('recipient',on_delete=models.CASCADE,related_name='Transaction_recipient')
    origin_account = models.ForeignKey('origin_account ',on_delete=models.CASCADE,related_name='Transaction_origin_account ')

class Card(models.Model):
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=20)
    date_issued = models.DateTimeField()
    CARD_CHOICES=(
        ('C','Credit Card'),
        ('D','Debit Card'),
    )
    card_type = models.CharField(max_length=20,choices=CARD_CHOICES)
    expiry_date = models.IntegerField()
    security_code = models.IntegerField()
    wallet = models.ManyToOneRel(Customer,on_delete=models.CASCADE,related_name='Card_wallet')
    account = models.ManyToManyRel(Customer,on_delete=models.CASCADE,related_name='Card_account')
    ISSUER_CHOICES=(
        ('v','Visa Card'),
        ('M','Master Card'),
    )
    issuer = models.CharField(max_length=20,choices=ISSUER_CHOICES)

class Thirdparty(models.Model):
    name = models.CharField(max_length=20)
    account_number = models.IntegerField()
    location = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    currency = models.ForeignKey('currency',on_delete=models.CASCADE,related_name='Thirdparty_currency')

class Notification(models.Model):
    MESSAGE_CHOICES=(
        ('E','Email'),
        ('P','Push'),
    )
    message = models.CharField(max_length=20,choices=MESSAGE_CHOICES)
    title = models.CharField(max_length=20)
    recipient = models.ForeignKey('recipient',on_delete=models.CASCADE,related_name='Notification_recipient')
    date_time = models.DateTimeField()
    STATUS_CHOICES=(
        ('R','Read'),
        ('U','Unread'),
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    bill_number = models.CharField(max_length=20)
    amount = models.IntegerField()
    account = models.ManyToManyField(Customer,on_delete=models.CASCADE,related_name='Card_account')
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    transaction = models.ManyToOneRel(Customer,on_delete=models.CASCADE,related_name='Loan_wallet')
    interest_rate = models.IntegerField()
    wallet = models.IntegerField()
    loan_balance = models.IntegerField()
    # guarantor = models.CharField(max_length=20)
    payment_due_date = models.DurationField()

class Reward(models.Model):
    name = models.CharField(max_length=20)
    customer_id = models.IntegerField()
    gender = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    points = models.IntegerField()
    third_party = models.ForeignKey('third_party',on_delete=models.CASCADE,related_name='Reward_third_party') 
    recipient = models.ForeignKey('recipient',on_delete=models.CASCADE,related_name='Reward_recipient') 
    points = models.IntegerField()
















          