from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserBankDetails)
admin.site.register(UserDocuments)
admin.site.register(UserAddress)