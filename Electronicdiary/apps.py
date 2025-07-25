from django.apps import AppConfig



class ElectronicdiaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Electronicdiary'

    def ready(self):
        import Electronicdiary.signals
