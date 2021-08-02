from apps.formulary.models import Formulary
from apps.formulary.api.serializers import FormularySerializer
from rest_framework.viewsets import ModelViewSet


class FormularyViewSet(ModelViewSet):
    """
        This class generates the raw methods that
        are displayed or consumed by the frontend

        - These methods are exposed to consume the form and the frontend -

    Args:
        ModelViewSet ([data models]): [
            The data from the already serialized database
            is called and the data is queried by making a 
            query that returns all
        ]
    """
    serializer_class = FormularySerializer
    queryset = Formulary.objects.all()
