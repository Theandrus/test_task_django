from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField('name of the category', max_length=73)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    number_of_sort = models.IntegerField()

    def __str__(self):
        return self.category_name


class Doctor(models.Model):
    doctor_name = models.CharField('name of the doctor', max_length=50)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField('description of this doctor')
    birth_date = models.DateTimeField('date of birth')
    experience = models.IntegerField('experience of the work')
    number_of_sort = models.IntegerField()

    def __str__(self):
        return self.doctor_name

    # def get_absolute_url(self):
    #     return reverse('doctor_name', kwargs={'doctor_slug': self.slug})


