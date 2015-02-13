from django.apps import AppConfig
from foodie.models import Vendor
from foodie.getData import getVendors, getEvents

class MyAppConfig(AppConfig):
    name = 'foodie'
    verbose_name = "Ginger Foodie"
    def ready(self):
        getVendors()
        getEvents()

