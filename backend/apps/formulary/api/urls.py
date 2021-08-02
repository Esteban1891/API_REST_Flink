"""This module is in charge of dynamically generating the corresponding paths
    To deploy them on endpoints
"""
from django.urls import path
from apps.formulary.api.api import FormularyViewSet
from rest_framework import routers

app_name = 'app'

router = routers.DefaultRouter()

router.register('formulary', FormularyViewSet, basename='formulary')

urlpatterns = router.urls
