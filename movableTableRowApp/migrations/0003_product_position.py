# Generated by Django 5.0.1 on 2024-02-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movableTableRowApp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]