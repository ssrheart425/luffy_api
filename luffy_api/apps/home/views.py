from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from django.conf import settings
from utils.common_mixin import APIListModelMixin
from .models import Banner
from .serializer import Bannerserializer
from django.conf import settings


class BannerView(GenericViewSet, APIListModelMixin):
    queryset = Banner.objects.all().filter(is_delete=False, is_show=True).order_by("orders")[0: settings.BANNER_COUNT]
    serializer_class = Bannerserializer
