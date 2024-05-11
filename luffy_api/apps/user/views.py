from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from utils.common_logger import logger
from utils.common_exception import PasswordException
from utils.common_response import APIResponse


class UserView(GenericViewSet):

    # @logger.catch
    def list(self, request):

        return APIResponse()
