from django.db import models
from authentication.models import *
from orders.models import *

# Create your models here.
class deliveryAssingment(models.Model):
    order = models.ForeignKey(orderDetails,on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(UserProfile,on_delete=models.CASCADE)




