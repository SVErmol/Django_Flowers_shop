# Generated by Django 3.2 on 2021-06-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='users',
            name='patronymic',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Фамилия'),
        ),
    ]