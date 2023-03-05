from django.urls import path, include
from rest_framework import routers
from apps.customer.api.v1.urls import router as customers_router_v1


router = routers.DefaultRouter()
router.registry.extend(customers_router_v1.registry)

urlpatterns = [
    path("api/v1/", include((router.urls, "v1"), namespace="customer")),
]
