from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "strongholdcoins"

    def ready(self):
        import_module("strongholdcoins.receivers")
