import factory

from django.contrib.auth import get_user_model

from .models import Account, Tree, PlantedTree


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating User instances.

    Attributes:
        username (str): A username that is automatically generated as a sequence of 'user0', 'user1', etc.
        password (str): A post-generation method call to set a default password for the user.
    """
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f'user{n}')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')


class AccountFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Account instances.

    Attributes:
        name (str): A name that is automatically generated as a sequence of 'account0', 'account1', etc.
        active (bool): A boolean flag that is set to True by default, indicating if the account is active.
    """
    class Meta:
        model = Account

    name = factory.Sequence(lambda n: f'account{n}')
    active = True


class TreeFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Tree instances.

    Attributes:
        name (str): A common name for the tree, generated as a sequence.
        scientific_name (str): A scientific name for the tree, generated as a sequence.
    """
    class Meta:
        model = Tree

    name = factory.Sequence(lambda n: f'Tree{n}')
    scientific_name = factory.Sequence(lambda n: f'Latin{n}')


class PlantedTreeFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating PlantedTree instances.

    Attributes:
        tree (ForeignKey): A ForeignKey to a Tree instance, created using the TreeFactory.
        user (ForeignKey): A ForeignKey to a User instance, created using the UserFactory.
        location (str): A fake address generated for the location of the planted tree.
        age (int): An integer representing the age of the tree, starting from 1 and incrementing for each subsequent tree.
    """
    class Meta:
        model = PlantedTree

    tree = factory.SubFactory(TreeFactory)
    user = factory.SubFactory(UserFactory)
    location = factory.Faker('address')  
    age = factory.Sequence(lambda n: n+1)
