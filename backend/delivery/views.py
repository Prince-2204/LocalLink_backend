from django.shortcuts import render
from authentication.auth_decorator import auth_required
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
@auth_required
def delivery_assingment(request):

    try:
        user = request.user
        
    except:
        pass

