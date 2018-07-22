import factory
from factory.django import DjangoModelFactory


class SiteFactory(DjangoModelFactory):

    class Meta:
        model = 'sites.Site'

    name = factory.Faker('name')


class ValuesFactory(DjangoModelFactory):

    class Meta:
        model = 'sites.Values'

    site = factory.SubFactory(SiteFactory)
    date = factory.Faker('date')
    a_value = factory.Faker('pyfloat')
    b_value = factory.Faker('pyfloat')
