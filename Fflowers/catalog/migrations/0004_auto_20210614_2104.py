# Generated by Django 3.2 on 2021-06-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_catalog_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='subcategory_id',
        ),
        migrations.AddField(
            model_name='catalog',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='catalog.subcategory'),
        ),
    ]
