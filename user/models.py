from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    ## Description 📝

    This model represents a custom user with additional methods for planting trees.

    ## Methods 📌

    - **plant_tree**(self, tree, location, age, account): Plant a single tree for the user at a specified location.
    - **plant_trees**(self, plantings): Plant multiple trees for the user at specified locations.
    """
    def plant_tree(self, tree, location, age, account):
        PlantedTree = apps.get_model('tree', 'PlantedTree')
        return PlantedTree.objects.create(
            user=self,
            tree=tree,
            location=location,
            age=age, 
            account=account,
        )
    
    def plant_trees(self, plantings):
        PlantedTree = apps.get_model('tree', 'PlantedTree')
        return [
            PlantedTree.objects.create(
                user=self,
                tree=planting[0],
                location=planting[1],
                age=planting[2],  
                account=planting[3]  
            ) for planting in plantings
        ]
    
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username