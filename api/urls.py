from django.urls import path
from api.views import API_Datawarehouse

urlpatterns = [
    path('', API_Datawarehouse.as_view())
]