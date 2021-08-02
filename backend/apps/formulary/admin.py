from django.contrib import admin
from apps.formulary.models import Formulary

"""[
    The model is called and registered
    in the administrative panel that has django by default
]
"""
admin.site.register(Formulary)
