from django.db import models
from django.contrib.auth import get_user_model


class PlantedTree(models.Model):
    """
    ## Description 📝

    This model represents a planted tree.

    ## Attributes 📌

    - **user** (**ForeignKey**): The user who planted the tree.
    - **tree** (**ForeignKey**): The type of tree that was planted.
    - **location** (**CharField**): The location where the tree was planted, stored as a string.
    - **age** (**IntegerField**): The age of the planted tree.
    - **planted_at** (**DateTimeField**): The datetime when the tree was planted.
    - **account** (**ForeignKey**): The account associated with the planted tree.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tree = models.ForeignKey('Tree', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)  
    age = models.IntegerField(default=1)
    planted_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Planted Tree")
        verbose_name_plural = ("Planted Trees")

    def __str__(self):
        return f'Tree {self.tree} - planted by {self.user}'    