# Generated by Django 5.0.1 on 2024-01-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borcivky', '0008_alter_product_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='banner',
            field=models.TextField(blank=True, null=True),
        ),
    ]
