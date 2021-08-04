from rest_framework import serializers
from apps.formulary.models import Formulary


class FormularySerializer(serializers.ModelSerializer):
    """[
        This class converts the data of the models
        in json and validates the exposed fields]

    Args:
        serializers ([type data field ]): [
            These fields are validated from 
            the serializer to expose automatic error 
            handling from here
        ]

    Raises:
        serializers.ValidationError: [It is validated that it only contains letters]
        serializers.ValidationError: [It is validated that it only contains letters]
        serializers.ValidationError: [Only capital letters are allowed]

    Returns:
        [type]: [description]
    """
    class Meta:
        model = Formulary
        fields = [
            'id',
            'name_company',
            'description_company',
            'symbol',
            'market_values'
        ]

    def validate(self, attrs):
        symbol = attrs.get('symbol', '')

        if not symbol.isupper():
            raise serializers.ValidationError(
                'Only capital letters are allowed for the symbol')

        return attrs
