# Generated by Django 5.0.1 on 2024-01-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borcivky', '0010_alter_product_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Ціна',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='Ціна2',
            field=models.IntegerField(),
        ),
    ]
