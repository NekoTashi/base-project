import factory

from v1.accounts.models.user import User
from django.contrib.auth.hashers import make_password


DEFAULT_TEST_PASSWORD = 'password'


class UserFactory(factory.DjangoModelFactory):

    email = factory.Sequence(lambda n: 'test_email_{}@email.test'.format(n))
    name = factory.Sequence(lambda n: 'test_name_{}'.format(n))
    password = make_password(DEFAULT_TEST_PASSWORD)

    class Meta:
        model = User
