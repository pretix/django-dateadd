# Generated by Django 3.1.5 on 2021-01-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('number_of_days', models.IntegerField(blank=True, null=True)),
                ('timedelta', models.DurationField(blank=True, null=True)),
            ],
        ),
    ]