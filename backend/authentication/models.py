from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_delivery_partner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, unique=True,db_index=True,default='1234567890')
    profile_image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user.username
    


class UserDocuments(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    aadhar_card = models.CharField(max_length=12, unique=True,db_index=True)
    pan_card = models.CharField(max_length=10, unique=True,db_index=True)
    aadhar_photo = models.ImageField(upload_to='aadhaar/')

    def __str__(self):
        return self.user_profile.user.username
    

class UserBankDetails(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=50, unique=True)
    ifsc_code = models.CharField(max_length=11)

    def __str__(self):
        return self.user_profile.user.username


class UserAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user_profile.user.username





