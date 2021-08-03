import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from apps.formulary.models import Formulary
from apps.formulary.api.serializers import FormularySerializer
from apps.formulary.api.api import FormularyViewSet


# initialize the APIClient app
client = Client()


class GetAllFormularyTest(TestCase):
    """ Test module for GET all formulary API """

    def setUp(self):
        Formulary.objects.create(
            name_company='Dow Jones industrial Average', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='KOOH', market_values=[
                10,
                20,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                200
            ])
        Formulary.objects.create(
            name_company='Dow Jones industrial Average', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='KOOH', market_values=[
                10,
                20,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                200
            ])
        Formulary.objects.create(
            name_company='Dow Jones industrial Average', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='KOOH', market_values=[
                10,
                20,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                200
            ])
        Formulary.objects.create(
            name_company='Dow Jones industrial Average', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='KOOH', market_values=[
                10,
                20,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                200
            ])

    def test_get_all_formulary(self):
        # get API response
        test = {
            "id": "ad841a2b-2a34-4f3b-ba43-ee5892dbc03b",
            "name_company": "string",
            "description_company": "string",
            "symbol": "HOLA",
            "market_values": [
                1,
                2
            ]
        }
        response = client.get(
            'http://143.198.58.196:8000/api/v1/formulary/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_put_all_formulary(self):
        # get API response
        test = {
            "id": "ad841a2b-2a34-4f3b-ba43-ee5892dbc03b",
            "name_company": "string",
            "description_company": "string",
            "symbol": "HOLA",
            "market_values": [
                1,
                2
            ]
        }
        response = client.put(
            'http://143.198.58.196:8000/api/v1/formulary/5d6c0df9-41bd-4e69-a75b-58cdbc53846f',
            test,
            format='json'
        )
        self.assertIsNot(response.status_code, status.HTTP_200_OK)