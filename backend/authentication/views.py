from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from django.contrib.auth.models import User
from .models import *
from django.conf import settings

def google_login(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)

    try:
        # Parse request body
        data = json.loads(request.body)
        token = data.get("token")
        email = data.get("email")
        name = data.get("name")

        if not token or not email:
            return JsonResponse({"error": "Token and email are required"}, status=400)

        # Verify token with Auth0
          
        response = requests.get(
            f"https://{settings.AUTH0_DOMAIN}/userinfo",
            headers={"Authorization": f"Bearer {token}"}
        )

        if response.status_code != 200:
            return JsonResponse({"error": "Invalid token"}, status=401)

        # Create or update the user
        user, created = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})

        return JsonResponse({
            "message": "User authenticated successfully",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.first_name,
                "is_new": created
            }
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def delivery_partner_details(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    
    try:
        token = request.POST.get("token")
        email = request.POST.get("email")
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        aadhar_card = request.POST.get("aadhar")
        pan_card = request.POST.get("pan")
        bank_name = request.POST.get("bank_name")
        account_number = request.POST.get("account_number")
        ifsc_code = request.POST.get("ifsc_code")
        profile_image = request.FILES.get("profile_image")
        aadhar_photo = request.FILES.get("aadhar_photo")

        if not token or not email:
            return JsonResponse({"error": "Token and email are required"}, status=400)
        
        
        response = requests.get(
            f"https://{settings.AUTH0_DOMAIN}/userinfo",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        if response.status_code != 200:
            return JsonResponse({"error": "Invalid token"}, status=401)
        
        user, created = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})
        
        user_profile, _ = UserProfile.objects.get_or_create(user=user, defaults={
            "phone_number": phone_number,
            "profile_image": profile_image,
            "is_delivery_partner": True
        })
        
        UserDocuments.objects.get_or_create(user_profile=user_profile, defaults={
            "aadhar_card": aadhar_card,
            "pan_card": pan_card,
            "aadhar_photo": aadhar_photo
        })
        
        UserBankDetails.objects.get_or_create(user_profile=user_profile, defaults={
            "bank_name": bank_name,
            "account_number": account_number,
            "ifsc_code": ifsc_code
        })
        
        return JsonResponse({"message": "Delivery partner details saved successfully"}, status=201)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


