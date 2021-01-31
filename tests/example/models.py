from django.db import models


class Product(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    timedelta = models.DurationField(blank=True, null=True)
    time_of_day = models.TimeField(blank=True, null=True)

