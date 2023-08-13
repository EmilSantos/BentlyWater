# Generated by Django 4.2.3 on 2023-08-08 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permitinformation', '0005_alter_property_unit_acres_alter_property_unit_cattle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cfs',
            field=models.FloatField(blank=True, null=True, verbose_name='C.F.S.'),
        ),
        migrations.AlterField(
            model_name='property',
            name='duty_af',
            field=models.FloatField(blank=True, null=True, verbose_name='Duty (AF)'),
        ),
    ]