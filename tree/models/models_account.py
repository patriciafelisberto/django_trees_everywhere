from django.db import models


class Account(models.Model):
    """
    ## Description 📝

     This model represents an account.

    ## Attributes 📌

    - **name** (**CharField**): The name of the account.
    - **created** (**DateTimeField**): The datetime when the account was created.
    - **active** (**BooleanField**): A flag indicating whether the account is active or not.
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return self.name        
