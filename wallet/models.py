from datetime import datetime
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name  = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    phone_number=models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.PositiveSmallIntegerField()
    password=models.CharField(max_length=20,null=True)
    id_number=models.IntegerField(null=True)
    nationality=models.CharField(max_length=20,null=True)
    # date_of_registration=models.DateTimeField()
    # profile_picture=models.ImageField(null=True)
    def __str__(self):
        return str(self.form)


class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='wallet_customer',null=True)
    amount = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20,null=True)
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency',null=True)
    pin = models.IntegerField(null=True)
    def __str__(self):
        return str(self.form)

class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20,null=True)
    account_balance = models.IntegerField()
    account_name = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='account_wallet',null=True)
    def __str__(self):
        return str(self.form)

#has some errors
class Transaction(models.Model):
    transaction_amount = models.IntegerField()
    transaction_number = models.CharField(max_length=20,null=True)
    transaction_type = models.CharField(max_length=20,null=True)
    transaction_charge = models.IntegerField()
    date_and_time = models.DateTimeField(default=datetime.now)
    destination_account = models.ForeignKey(to=Account,on_delete=models.CASCADE,related_name='destination_account',null=True)
    reciept = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='transaction_wallet',null=True)
    origin_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='origin_account',null=True)
    def __str__(self):
        return str(self.form)

class Card(models.Model):
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=20,null=True)
    date_issued = models.DateTimeField(default=datetime.now)
    CARD_CHOICES=(
        ('C','Credit Card'),
        ('D','Debit Card'),
    )
    card_type = models.CharField(max_length=20,choices=CARD_CHOICES,null=True)
    expiry_date = models.IntegerField()
    security_code = models.IntegerField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='card_wallet',null=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='card_account',null=True)
    ISSUER_CHOICES=(
        ('v','Visa Card'),
        ('M','Master Card'),
    )
    issuer = models.CharField(max_length=20,choices=ISSUER_CHOICES,null=True)
    def __str__(self):
        return str(self.form)

class Currency(models.Model):
    country = models.CharField(max_length=30,null=True)
    symbol = models.CharField(max_length=5,null=True)
    amount = models.IntegerField()
    def __str__(self):
        return str(self.form)

class Thirdparty(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='third_transaction',null=True)
    name = models.CharField(max_length=20,null=True)
    account_number = models.IntegerField(null=True)
    location = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='thirdparty_currency',null=True)
    def __str__(self):
        return str(self.form)


class Notification(models.Model):
    MESSAGE_CHOICES=(
        ('E','Email'),
        ('P','Push'),
    )
    message = models.CharField(max_length=20,choices=MESSAGE_CHOICES,null=True)
    # title = models.CharField(max_length=20,null=True)
    recipient = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='notification_recipient',null=True)
    date_time = models.DateTimeField(default=datetime.now)
    STATUS_CHOICES=(
        ('R','Read'),
        ('U','Unread'),
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,null=True)
    def __str__(self):
        return str(self.form)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=20,null=True)
    date = models.DateTimeField(default=datetime.now)
    bill_number = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='receipt_customer',null=True)
    receipt_file = models.FileField()
    def __str__(self):
        return str(self.form)

class Loan(models.Model):
    loan_type = models.CharField(max_length=20,null=True)
    amount = models.IntegerField()
    interest_rate = models.IntegerField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='loan_wallet',null=True)
    loan_balance = models.IntegerField()
    guarantor = models.CharField(max_length=20,null=True)
    payment_due_date = models.DurationField()
    def __str__(self):
        return str(self.form)

#Has some errors
class Reward(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='reward_transaction',null=True)
    customer_id = models.IntegerField()
    message = models.CharField(max_length=50,null=True)
    date_time = models.DateTimeField(default=datetime.now)
    points = models.IntegerField() 
    recipient = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='reward_recipient',null=True) 
    def __str__(self):
        return str(self.form)















          