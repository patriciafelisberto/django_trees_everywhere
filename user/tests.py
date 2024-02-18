from django.test import TestCase
from tree.models import PlantedTree

from tree.factories import AccountFactory, UserFactory, TreeFactory


class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.tree = TreeFactory()
        self.account = AccountFactory()  # Criando uma conta para usar nos testes

    def test_plant_tree_method(self):
        """
        Test the plant_tree method to ensure it creates a PlantedTree instance
        associated with the user and an account.
        """
        location = 'Sample Location'
        age = 5  # Setting an age for the tree
        # Adding the account parameter when calling plant_tree
        self.user.plant_tree(self.tree, location, age, self.account)

        # Verify that a PlantedTree has been created and is associated with the user and account
        self.assertEqual(PlantedTree.objects.count(), 1)
        planted_tree = PlantedTree.objects.first()
        self.assertEqual(planted_tree.user, self.user)
        self.assertEqual(planted_tree.tree, self.tree)
        self.assertEqual(planted_tree.age, age)
        self.assertEqual(planted_tree.account, self.account) 

    def test_plant_trees_method(self):
        """
        Test the plant_trees method to ensure it creates multiple PlantedTree instances
        associated with the user and accounts.
        """
        plantings = [
            (self.tree, 'Location 1', 5, self.account),
            (TreeFactory(), 'Location 2', 10, self.account)
        ]
        # Adding the account parameter when calling plant_trees
        self.user.plant_trees(plantings)

        # Check that two PlantedTrees have been created and are associated with the user and account
        self.assertEqual(PlantedTree.objects.count(), 2)
        self.assertEqual(PlantedTree.objects.filter(user=self.user, account=self.account).count(), 2)

