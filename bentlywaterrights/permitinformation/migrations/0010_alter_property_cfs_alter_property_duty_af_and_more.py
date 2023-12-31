# Generated by Django 4.2.3 on 2023-08-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permitinformation', '0009_alter_property_unit_acres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cfs',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='C.F.S.'),
        ),
        migrations.AlterField(
            model_name='property',
            name='duty_af',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Duty (AF)'),
        ),
        migrations.AlterField(
            model_name='property',
            name='remarks',
            field=models.CharField(blank=True, max_length=150, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='property',
            name='sale_value',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sale Value'),
        ),
        migrations.AlterField(
            model_name='property',
            name='source',
            field=models.CharField(blank=True, max_length=10, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='property',
            name='unit_acres',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Acres'),
        ),
        migrations.AlterField(
            model_name='property',
            name='use',
            field=models.CharField(blank=True, max_length=10, verbose_name='Use'),
        ),
    ]
