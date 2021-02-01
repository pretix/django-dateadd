#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-dateadd
------------

Tests for `django-dateadd` models module.
"""
import datetime
import pytz

from django.db.models import DateTimeField, F, ExpressionWrapper
from django.db.models.functions import TruncDay
from django.test import TestCase
from django.utils import timezone

from django_dateadd import models
from tests.example.models import Product


class TestDjango_dateadd(TestCase):

    def setUp(self):
        self.eastern = pytz.timezone('US/Eastern')
        someday = self.eastern.localize(datetime.datetime(2021, 2, 25, 23, 00))
        Product.objects.create(
            start_date=someday,
            number_of_days=3,
            timedelta=datetime.timedelta(hours=10),
            time_of_day=datetime.time(hour=10)
        )

    def test_day_arithmetics_with_timedelta(self):
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) - datetime.timedelta(days=3),
                output_field=DateTimeField()
            )
        )

        # The following test will pass on PostgreSQL but fail on SQLite
        # The latter will return the same datetime, but mark it as UTC for some reason
        expected = datetime.datetime(2021, 2, 22, 0)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_day_arithmetics_with_integer(self):
        # This will work only on PostgreSQL and not on SQLite
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) - F('number_of_days') * datetime.timedelta(days=1),
                output_field=DateTimeField()
            )
        )

        expected = datetime.datetime(2021, 2, 22, 0)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_time_arithmetics_with_time(self):
        # This will work only on PostgreSQL and not on SQLite
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) + F('time_of_day'),
                output_field=DateTimeField()
            )
        )

        expected = datetime.datetime(2021, 2, 25, 10)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_time_arithmetics_with_timedelta(self):
        # This will work only on PostgreSQL and not on SQLite
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) + F('timedelta'),
                output_field=DateTimeField()
            )
        )

        expected = datetime.datetime(2021, 2, 25, 10)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_datetime_arithmetics(self):
        # This will work only on PostgreSQL and not on SQLite
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) - F('number_of_days') * datetime.timedelta(days=1) +F('time_of_day'),
                output_field=DateTimeField()
            )
        )

        expected = datetime.datetime(2021, 2, 22, 10)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_datetime_arithmetics_with_timedelta(self):
        products = Product.objects.all().annotate(
            calculated=ExpressionWrapper(
                TruncDay('start_date', tzinfo=self.eastern) - datetime.timedelta(days=3) + F('timedelta'),
                output_field=DateTimeField()
            )
        )

        # The following test will pass on PostgreSQL but fail on SQLite
        # The latter will return the same datetime, but mark it as UTC for some reason
        expected = datetime.datetime(2021, 2, 22, 10)
        self.assertEqual(products[0].calculated, expected)
        # Note that on PostgreSQL the while returned datetime is using the correct timezone (otherwise the result would be
        # datetime.datetime(2021, 2, 23, 0)
        # ), the datetime is naive. You can see by uncommenting the following test which will fail:

        # self.assertTrue(timezone.is_aware(products[0].calculated))

    def test_truncday_timezone(self):
        products = Product.objects.all().annotate(
            calculated=TruncDay('start_date', tzinfo=self.eastern)
        )
        expected = self.eastern.localize(datetime.datetime(2021, 2, 25, 0))
        self.assertEqual(products[0].calculated, expected)
