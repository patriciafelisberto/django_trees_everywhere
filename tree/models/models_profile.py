from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """
    ## Description 📝

    This model represents a user profile.

    ## Attributes 📌

    - **user** (**OneToOneField**): The user associated with the profile.
    - **about** (**TextField**): Information about the user.
    - **joined** (**DateTimeField**): The datetime when the user joined.
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return f'Profile {self.user}'