from django.test import TestCase

from .models import PlantedTree
from .factories import UserFactory, AccountFactory, PlantedTreeFactory, TreeFactory


class PlantingTestCase(TestCase):
    """
    The PlantingTestCase class contains tests to ensure that accounts, users,
    and trees can be created and that the planted trees are correctly associated
    with the respective accounts and users.
    """
    def test_create_accounts_and_plantings(self):
        """
        Test the creation of accounts, users, and trees, and the association of 
        planted trees with users and accounts. It verifies the counts of planted 
        trees and checks the correct associations to users and accounts.
        """
        # Create accounts
        account1 = AccountFactory()
        account2 = AccountFactory()
        
        # Create users
        user1 = UserFactory()
        user2 = UserFactory()
        user3 = UserFactory()
        
        # Create trees
        tree1 = TreeFactory()
        tree2 = TreeFactory()
        
        # Plant trees by associating them with users and accounts
        planted_tree1 = PlantedTreeFactory(user=user1, tree=tree1, account=account1)
        planted_tree2 = PlantedTreeFactory(user=user2, tree=tree2, account=account1)
        planted_tree3 = PlantedTreeFactory(user=user3, tree=tree1, account=account2)

        # Check if the planted trees were created
        self.assertEqual(PlantedTree.objects.count(), 3)

        # Check if trees are correctly associated with accounts
        self.assertEqual(account1.plantedtree_set.count(), 2)
        self.assertEqual(account2.plantedtree_set.count(), 1)

        # Check if trees are correctly associated with users
        self.assertIn(planted_tree1, user1.plantedtree_set.all())
        self.assertIn(planted_tree2, user2.plantedtree_set.all())
        self.assertIn(planted_tree3, user3.plantedtree_set.all())
