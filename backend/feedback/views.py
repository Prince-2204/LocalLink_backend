from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def user_feedback(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    
    try:
        data = json.load(request.body)
        token = data.get("token")
        

    except:
        pass