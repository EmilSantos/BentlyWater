# Generated by Django 4.2.3 on 2023-08-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permitinformation', '0010_alter_property_cfs_alter_property_duty_af_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='unit_acres',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Acres'),
        ),
        migrations.AlterField(
            model_name='property',
            name='unit_other',
            field=models.CharField(blank=True, max_length=100, verbose_name='Other'),
        ),
    ]