from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import Thirdparty
from .models import Notification
from .models import Recipient
from .models import Loan
from .models import Reward


class CustomerADMIN(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name','last_name',)

admin.site.register(Customer,CustomerADMIN)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Recipient)
admin.site.register(Loan)
admin.site.register(Reward)








 