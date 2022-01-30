# Generated by Django 3.2 on 2021-06-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='data_delete',
            field=models.DateField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name_product',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='show',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='subcategory_id',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='id категории'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='suplier_id',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='id поставщика'),
        ),
    ]