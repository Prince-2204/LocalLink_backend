from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('auth/login',google_login,name="login"),
    path('auth/deliveryDetails',delivery_partner_details,name='deliveryPartner'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)