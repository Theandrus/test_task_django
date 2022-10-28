# Generated by Django 3.2.16 on 2022-10-20 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=73, verbose_name='name of the category')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('number_of_sort', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50, verbose_name='name of the doctor')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='description of this doctor')),
                ('birth_date', models.DateTimeField(verbose_name='date of birth')),
                ('experience', models.IntegerField(verbose_name='experience of the work')),
                ('number_of_sort', models.BooleanField(null=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.category')),
            ],
        ),
    ]