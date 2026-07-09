# -*- coding: utf-8 -*-
from django.test import TestCase
from core.templatetags.misc import next as next_filter, prev as prev_filter


class TestMiscTemplateTags(TestCase):
    def test_next_filter(self):
        sample_list = ["a", "b", "c"]
        self.assertEqual(next_filter(sample_list, 0), "b")
        self.assertEqual(next_filter(sample_list, 1), "c")
        self.assertEqual(next_filter(sample_list, 2), "")
        self.assertEqual(next_filter(sample_list, 3), "")
        self.assertEqual(next_filter([], 0), "")
        self.assertEqual(next_filter(None, 0), "")

    def test_prev_filter(self):
        sample_list = ["a", "b", "c"]
        self.assertEqual(prev_filter(sample_list, 2), "b")
        self.assertEqual(prev_filter(sample_list, 1), "a")
        self.assertEqual(prev_filter(sample_list, 0), "")
        self.assertEqual(prev_filter(sample_list, -1), "")
        self.assertEqual(prev_filter([], 0), "")
        self.assertEqual(prev_filter(None, 0), "")
