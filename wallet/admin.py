from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import Thirdparty
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward


class CustomerADMIN(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name','last_name',)

class WalletADMIN(admin.ModelAdmin):
    list_display = ('balance','time','amount',)
    search_fields = ('time','amount',)

class AccountADMIN(admin.ModelAdmin):
    list_display = ('account_name','account_balance','account_number',)
    search_fields = ('number','balance',)

class TransactionADMIN(admin.ModelAdmin):
    list_display = ('transaction_name','transaction_ref','date_and_time',)
    search_fields = ('transaction_ref','transaction_name',)  

class CardADMIN(admin.ModelAdmin):
    list_display = ('card_name','security_code','card_number',)
    search_fields = ('security_code','card_number',)

class ThirdpartyADMIN(admin.ModelAdmin):
    list_display = ('name','account','location',)
    search_fields = ('name','account',)

class NotificationADMIN(admin.ModelAdmin):
    list_display = ('message','date_time','title',)
    search_fields = ('message','date_time',)

class ReceiptADMIN(admin.ModelAdmin):
    list_display = ('bill_number','amount','date_time',)
    search_fields = ('bill_number','amount',)

class LoanADMIN(admin.ModelAdmin):
    list_display = ('guarantor','amount','loan_type',)
    search_fields = ('guarantor','amount',)

class RewardADMIN(admin.ModelAdmin):
    list_display = ('customer_id','message','gender',)
    search_fields = ('customer_id','message',)    

admin.site.register(Customer,CustomerADMIN)
admin.site.register(Wallet, WalletADMIN)
admin.site.register(Account, AccountADMIN)
admin.site.register(Transaction, TransactionADMIN)
admin.site.register(Card, CardADMIN)
admin.site.register(Thirdparty, ThirdpartyADMIN)
admin.site.register(Notification, NotificationADMIN)
admin.site.register(Receipt, ReceiptADMIN)
admin.site.register(Loan, LoanADMIN)
admin.site.register(Reward, RewardADMIN)








 