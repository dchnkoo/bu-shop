# Generated by Django 5.0.1 on 2024-01-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borcivky', '0009_alter_bannerimage_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='first',
            field=models.TextField(blank=True, null=True),
        ),
    ]
