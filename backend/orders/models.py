from django.db import models
from authentication.models import UserProfile
from django.utils import timezone
import uuid
# Create your models here.
class orderDetails(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order_number = models.BigAutoField(primary_key=True) 
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_details = models.CharField(max_length=200)
    pickup = models.CharField(max_length=400)
    dropoff = models.CharField(max_length=400)
    delivery_deadline = models.CharField(max_length=200)
    budget = models.IntegerField()
    status = models.CharField(max_length=20, default="Pending", choices=[
        ("Pending", "Pending"),
        ("in-progress", "in-progress"),
        ("Completed", "Completed"),
    ])


    def __str__(self):
        return f"{self.order_number} {self.user.user.username}"
    

