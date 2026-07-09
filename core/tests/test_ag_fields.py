# -*- coding: utf-8 -*-
import datetime as dt
from unittest.mock import PropertyMock, patch

from django.test import TestCase
from django.core.exceptions import ValidationError

from core.fields import NapStartMaxTimeField, NapStartMinTimeField


class MockSettings:
    nap_start_min = dt.time(12, 0)
    nap_start_max = dt.time(15, 0)


class TestCoreFields(TestCase):
    @patch(
        "core.models.Sleep.settings",
        new_callable=PropertyMock,
        return_value=MockSettings(),
    )
    def test_nap_start_max_time_field(self, mock_settings):
        field = NapStartMaxTimeField()
        # Should raise ValidationError if value < nap_start_min
        with self.assertRaises(ValidationError):
            field.validate(dt.time(11, 0))

        # Should not raise exception
        field.validate(dt.time(13, 0))

    @patch(
        "core.models.Sleep.settings",
        new_callable=PropertyMock,
        return_value=MockSettings(),
    )
    def test_nap_start_min_time_field(self, mock_settings):
        field = NapStartMinTimeField()
        # Should raise ValidationError if value > nap_start_max
        with self.assertRaises(ValidationError):
            field.validate(dt.time(16, 0))

        # Should not raise exception
        field.validate(dt.time(14, 0))
