from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.customer.api.v1.views import CustomerViewSet


router = DefaultRouter()
router.register("customers", CustomerViewSet)
