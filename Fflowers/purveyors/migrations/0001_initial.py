# Generated by Django 3.2 on 2021-06-17 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purveyors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Название')),
                ('address', models.CharField(blank=True, max_length=400, null=True, verbose_name='Адрес')),
                ('data_delete', models.DateField(blank=True, null=True, verbose_name='Дата удаления')),
            ],
        ),
    ]
