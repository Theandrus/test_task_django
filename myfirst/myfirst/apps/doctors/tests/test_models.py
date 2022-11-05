from django.test import TestCase

from ..models import Category, Doctor


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category_name='Cardiology', slug='cardiology', number_of_sort=15)

    def test_category_name(self):
        name = Category.objects.get(id=2)
        field_label = name.get_field('category_name')
        self.assertEqual(field_label, 'Dentist')

    def test_category_name_max_length(self):
        name = Category.objects.get(id=2)
        max_length = name.get_field('category_name').max_length
        self.assertEqual(max_length, 73)


class DoctorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Doctor.objects.create(doctor_name='Anton', slug='anton', categories='Dentist', description='kdvfbhk',
                              birth_date='2017-11-23 13:23', experience=4, number_of_sort=15)

    def test_doctor_name(self):
        name = Doctor.objects.get(id=4)
        field_label = name.get_field('doctor_name')
        self.assertEqual(field_label, 'Andrii')

    def test_doctor_name_max_length(self):
        name = Doctor.objects.get(id=4)
        max_length = name.get_field('doctor_name').max_length
        self.assertEqual(max_length, 50)

    def test_slug(self):
        name = Doctor.objects.get(id=4)
        field_label = name.get_field('slug')
        self.assertEqual(field_label, 'andrii')

    def test_experience(self):
        name = Doctor.objects.get(id=4)
        field_label = name.get_field('experience')
        self.assertEqual(field_label, 3)








