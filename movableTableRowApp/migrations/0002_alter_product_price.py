# Generated by Django 5.0.1 on 2024-02-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movableTableRowApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
