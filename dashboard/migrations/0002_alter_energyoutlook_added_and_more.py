# Generated by Django 4.2.4 on 2023-08-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyoutlook',
            name='added',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='energyoutlook',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]
