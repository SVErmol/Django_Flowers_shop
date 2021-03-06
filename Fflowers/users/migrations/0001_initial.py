# Generated by Django 3.2 on 2021-06-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=400, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=400, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=400, verbose_name='Отчество')),
                ('position', models.IntegerField(blank=True, choices=[(1, 'Администратор'), (2, 'Флорист'), (3, 'Курьер')], default=1, null=True, verbose_name='Должность')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер')),
                ('note', models.TextField(verbose_name='Комментарий')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('data_delete', models.DateField(blank=True, null=True, verbose_name='Дата удаления')),
            ],
        ),
    ]
