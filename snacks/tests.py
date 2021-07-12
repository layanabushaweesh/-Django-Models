from django.test import TestCase

from django.urls import reverse


# Create your tests here.
class Tests(TestCase):
    def test_snack_list_1(self):

        url = reverse('snack_list')
        actuall = self.client.get(url)
        expected=200
        self.assertEqual(actuall.status_code, expected)

    def test_snack_list_template(self):

        url = reverse('snack_list')
        respons = self.client.get(url)
        self.assertTemplateUsed(respons, 'snack_list.html')
        self.assertTemplateUsed(respons, 'base.html')