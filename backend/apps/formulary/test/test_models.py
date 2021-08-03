from django.test import TestCase
from apps.formulary.models import Formulary


class FormularyTest(TestCase):
    """ Test module for Formulary model """

    def setUp(self):
        Formulary.objects.create(
            id='a49f515a-83b8-48f2-993e-21e529bed82e', name_company='Dow Jones industrial Average', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='KOOH', market_values=[
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
            id='4c0f3893-6070-491e-875f-a8ccf25fafbc', name_company='NIKE, inc.', description_company='Koombea INC is an American digital product development company, established in 2007.', symbol='NKE', market_values=[
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

    def test_formulary_symbol(self):
        formulary_dow_jones = Formulary.objects.get(symbol='KOOH')
        formulary_nike = Formulary.objects.get(symbol='NKE')
        self.assertEqual(
            formulary_dow_jones.get_symbol(), "Dow Jones industrial Average Has as symbol KOOH")
        self.assertEqual(
            formulary_nike.get_symbol(), "NIKE, inc. Has as symbol NKE")
