# Generated by Django 4.2.7 on 2023-11-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
