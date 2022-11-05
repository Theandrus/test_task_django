from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from myfirst.myfirst.apps.doctors.models import Category


class DoctorsApiTestCase(APITestCase):

    def test_get(self):
        doctor = Category.objects.create(category_name='Bobi', slug='bobi', number_of_sort=2)
        url = reverse('main')
        print(url)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print(response)
