# Generated by Django 4.1.7 on 2023-03-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_building_street_building_town_building_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='zip_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]