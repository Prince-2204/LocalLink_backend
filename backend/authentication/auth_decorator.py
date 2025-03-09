from django.http import JsonResponse
from functools import wraps
from django.contrib.auth import get_user_model
from django.conf import settings
import requests

User = get_user_model()

def auth_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing or invalid token"}, status=401)

        token = auth_header.split(" ")[1]

        # Verify the token with Auth0
        response = requests.get(
            f"https://{settings.AUTH0_DOMAIN}/userinfo",
            headers={"Authorization": f"Bearer {token}"},
        )

        if response.status_code != 200:
            return JsonResponse({"error": "Invalid token"}, status=401)

        # Extract user info
        user_data = response.json()
        email = user_data.get("email")
        name = user_data.get("name")

        # Create or fetch the user
        user, _ = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})

        # Attach the user to the request
        request.user = user

        return view_func(request, *args, **kwargs)

    return wrapper

