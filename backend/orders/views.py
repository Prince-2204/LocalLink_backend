from django.shortcuts import render
from authentication.auth_decorator import auth_required
from rest_framework.decorators import api_view
from orders.models import *
import json
from authentication.models import UserProfile
from orders.models import *
from django.http import JsonResponse

# Create your views here.
@auth_required
@api_view(["POST"])
def order_details(request):

    try:
        user = request.user
        item_name = request.POST.get("itemName")
        item_details = request.POST.get("description")
        pickup = request.POST.get("pickup")
        dropoff = request.POST.get("dropoff")
        delivery_deadline = request.POST.get("deliveryDeadline")
        budget_char = request.POST.get("budget")
        budget = int(budget_char)
        status = request.POST.get("status")
        user_profile = UserProfile.objects.get(user=user)
        orderDetails.objects.create(
            user = user_profile,
            user = user_profile,
            item_name = item_name,
            item_details = item_details,
            pickup = pickup,
            dropoff = dropoff,
            delivery_deadline = delivery_deadline,
            budget = budget,
            status = status
        )
        return JsonResponse({"success":"Order Placed successfully"},status=200)


    except:
        return JsonResponse({"error":"Eroor while placing order"},status=400)
    