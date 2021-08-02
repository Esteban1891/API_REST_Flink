from django.apps import AppConfig


class FormularyConfig(AppConfig):
    """[Load the path where it can be called in settings]

    Args:
        AppConfig ([call]): [call app]
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'formulary'
