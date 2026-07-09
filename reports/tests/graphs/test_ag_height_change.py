# -*- coding: utf-8 -*-
import datetime as dt

from django.test import TestCase
from django.utils import timezone

from core import models
from reports.graphs.height_change import height_change


class TestHeightChangeGraph(TestCase):
    def test_height_change_no_data(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        # Empty querysets
        actual = models.Height.objects.none()
        percentiles = models.HeightPercentile.objects.none()

        result = height_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)

    def test_height_change_with_data(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        models.Height.objects.create(child=c, date=dt.date(2020, 1, 10), height=50.0)
        models.Height.objects.create(child=c, date=dt.date(2020, 2, 10), height=55.0)

        actual = models.Height.objects.filter(child=c)
        percentiles = models.HeightPercentile.objects.none()

        result = height_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)

    def test_height_change_with_percentiles(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        models.Height.objects.create(child=c, date=dt.date(2020, 1, 10), height=50.0)

        # mock some percentiles
        models.HeightPercentile.objects.create(
            sex="F",
            age_in_days=dt.timedelta(days=5),
            p3_height=48,
            p15_height=49,
            p50_height=50,
            p85_height=51,
            p97_height=52,
        )
        models.HeightPercentile.objects.create(
            sex="F",
            age_in_days=dt.timedelta(days=15),
            p3_height=50,
            p15_height=51,
            p50_height=52,
            p85_height=53,
            p97_height=54,
        )

        actual = models.Height.objects.filter(child=c)
        percentiles = models.HeightPercentile.objects.all()

        result = height_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)
