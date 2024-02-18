from django.db import models


class Tree(models.Model):
    """
    ## Description 📝

    This model represents a tree.

    ## Attributes 📌

    - **name** (**CharField**): The common name of the tree.
    - **scientific_name** (**CharField**): The scientific name of the tree.
    """
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("Tree")
        verbose_name_plural = ("Trees")

    def __str__(self):
        return self.name    