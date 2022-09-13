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
from .models import Currency


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields =('first_name','last_name','age','email',)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance',Customer,'amount',)
    search_fields =  ('balance',Customer,'amount',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','account_balance','account_number',)
    search_fields =  ('account_name','account_balance','account_number',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_amount','transaction_number','transaction_type',)
    search_fields = ('transaction_amount','transaction_number','transaction_type',) 

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name','date_issued','card_number',)
    search_fields =('card_name','date_issued','card_number',)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display = ('name','account_number','location',)
    search_fields =  ('name','account_number','location',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message','date_time',)
    search_fields =('message','date_time',)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('bill_number','amount','date',)
    search_fields = ('bill_number','amount','date',)

class LoanAdmin(admin.ModelAdmin):
    list_display = (Customer,'amount','loan_type',)
    search_fields = (Customer,'amount','loan_type',)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('customer_id','message',Transaction,)
    search_fields =('customer_id','message',Transaction,)    

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country','symbol','amount',)
    search_fields = ('country','symbol','amount',) 

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Thirdparty, ThirdpartyAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(Currency, CurrencyAdmin)








 