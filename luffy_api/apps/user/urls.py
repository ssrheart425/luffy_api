from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserView

router = SimpleRouter()
router.register("test", UserView, "test")

urlpatterns = [
    path("", include(router.urls)),
]
