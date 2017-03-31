from django.contrib import admin

from .models import Category
from .models import Transaction
from .models import Account

admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Account)
