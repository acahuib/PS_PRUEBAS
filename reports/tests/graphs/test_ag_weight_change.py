# -*- coding: utf-8 -*-
import datetime as dt

from django.test import TestCase

from core import models
from reports.graphs.weight_change import weight_change


class TestWeightChangeGraph(TestCase):
    def test_weight_change_no_data(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        actual = models.Weight.objects.none()
        percentiles = models.WeightPercentile.objects.none()

        result = weight_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)

    def test_weight_change_with_data(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        models.Weight.objects.create(child=c, date=dt.date(2020, 1, 10), weight=4.0)
        models.Weight.objects.create(child=c, date=dt.date(2020, 2, 10), weight=5.0)

        actual = models.Weight.objects.filter(child=c)
        percentiles = models.WeightPercentile.objects.none()

        result = weight_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)

    def test_weight_change_with_percentiles(self):
        c = models.Child.objects.create(
            first_name="Test", last_name="Child", birth_date=dt.date(2020, 1, 1)
        )
        models.Weight.objects.create(child=c, date=dt.date(2020, 1, 10), weight=4.0)

        models.WeightPercentile.objects.create(
            sex="F",
            age_in_days=dt.timedelta(days=5),
            p3_weight=3.5,
            p15_weight=3.8,
            p50_weight=4.0,
            p85_weight=4.2,
            p97_weight=4.5,
        )
        models.WeightPercentile.objects.create(
            sex="F",
            age_in_days=dt.timedelta(days=15),
            p3_weight=3.8,
            p15_weight=4.0,
            p50_weight=4.2,
            p85_weight=4.5,
            p97_weight=4.8,
        )

        actual = models.Weight.objects.filter(child=c)
        percentiles = models.WeightPercentile.objects.all()

        result = weight_change(actual, percentiles, c.birth_date)
        self.assertIsNotNone(result)
