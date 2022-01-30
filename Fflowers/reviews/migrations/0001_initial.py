# Generated by Django 3.2 on 2021-06-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=400, verbose_name='ID продукта')),
                ('review_text', models.CharField(max_length=400, verbose_name='Текст')),
                ('name_client', models.CharField(max_length=400, verbose_name='Имя')),
                ('data', models.DateField(verbose_name='Дата')),
                ('photo', models.FileField(upload_to='static/main/image')),
                ('data_delete', models.DateField(null=True, verbose_name='Дата удаления')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'managed': True,
            },
        ),
    ]
