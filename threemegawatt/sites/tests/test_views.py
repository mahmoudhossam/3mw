from django.test import TestCase
from django.urls import reverse
from .factories import SiteFactory
from ..models import Site


class SiteDetailTest(TestCase):

    def test_valid_site(self):
        SiteFactory.create()
        response = self.client.get(reverse('detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_invalid_site(self):
        response = self.client.get(reverse('detail', args=[99]))
        self.assertEqual(response.status_code, 404)


class SiteListTest(TestCase):

    def test_site_listing(self):
        response = self.client.get('/')
        self.assertQuerysetEqual(response.context['sites'], Site.objects.all())
        self.assertEqual(response.status_code, 200)
