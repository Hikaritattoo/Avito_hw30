import factory

from ads.models import Ad
from tests.factories.category import CategoryFactory
from tests.factories.user import UserFactory


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = 'Test 10 characters minimum'
    price = 1000

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
