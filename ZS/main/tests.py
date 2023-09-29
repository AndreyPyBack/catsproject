# from django.test import SimpleTestCase
#
#
# class SimpleTests(SimpleTestCase):
#     class TransactionTestCase:
#         def test_main_page_status_code(self):
#             response = self.client.get('/')
#             self.assertEqual(response.statpus_code, 300)
from django.test import TestCase

from .models import Cats


class CatsTestCase(TestCase):
    def setUp(self):
        self.cats = Cats.objects.create(
        name='Test',
        color='Test',
        eyes='Test',
        text_cat=4
        )

    def test_training_name(self):
        self.assertEqual(str(self.cats.name),'Test')

    def test_training_color(self):
        self.assertEqual(str(self.cats.color),'Test')

    def test_training_eyes(self):
        self.assertEqual(str(self.cats.eyes),'Test')

    def test_training_text_cat(self):
        self.assertEqual(int(self.cats.text_cat), 4)