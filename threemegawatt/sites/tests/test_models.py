from django.test import TestCase
from .factories import SiteFactory, ValuesFactory
from ..models import Site, Values


class SiteTests(TestCase):

    def test_create_site(self):
        SiteFactory.create()
        self.assertEqual(Site.objects.count(), 1)


class ValuesTests(TestCase):

    def test_create_values(self):
        ValuesFactory.create()
        self.assertEqual(Values.objects.count(), 1)


class ValuesManagerTests(TestCase):

    def setUp(self):
        self.site1 = SiteFactory.create()
        self.site2 = SiteFactory.create()
        ValuesFactory.create(site=self.site1, a_value=2.0,
                             b_value=3.0)
        ValuesFactory.create(site=self.site1, a_value=1.0,
                             b_value=2.0)
        ValuesFactory.create(site=self.site2, a_value=4.0,
                             b_value=3.0)
        ValuesFactory.create(site=self.site2, a_value=2.0,
                             b_value=1.0)

    def test_sum(self):
        expected = {self.site1.name: {'a_value': 3.0,
                                      'b_value': 5.0},
                    self.site2.name: {'a_value': 6.0,
                                      'b_value': 4.0}}
        actual = Values.objects.sum()
        self.assertEqual(actual, expected)

    def test_average(self):
        actual = Values.objects.average()
        self.assertEqual(actual[0].a_value, 1.5)
        self.assertEqual(actual[0].b_value, 2.5)
        self.assertEqual(actual[1].a_value, 3)
        self.assertEqual(actual[1].b_value, 2.0)
