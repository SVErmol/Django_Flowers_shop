# Generated by Django 3.2 on 2021-06-19 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purveyors', '0001_initial'),
        ('catalog', '0007_auto_20210619_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='suplier_id',
        ),
        migrations.AddField(
            model_name='catalog',
            name='purveyor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purveyor', to='purveyors.purveyors'),
        ),
    ]
