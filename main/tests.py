from django.test import TestCase
from django.test import TestCase, Client
from main.models import Flower

# tidak mendapatkan nilai bonus apabila kamu 
# #mengimplementasikan testing pengecekan berjalannya URL di
# aplikasi dan penggunaan template yang sesuai.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class FlowerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Flower.objects.create(name='Lily', amount='4')

    def test_name_label(self):
        flower = Flower.objects.get(id=1)
        field_label = flower._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_amount_label(self):
        flower = Flower.objects.get(id=1)
        field_label = flower._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')
