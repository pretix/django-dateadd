# Generated by Django 3.1.5 on 2021-01-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_of_day',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
