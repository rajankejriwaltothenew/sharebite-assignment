from django.db import models


class Section(models.Model):
    """This class is used to store details for section."""

    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        """Function for str."""
        return "{}<{}>".format(str(self.name), str(self.id))


class Item(models.Model):
    """This class is used to store details for items of the menu."""

    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    section = models.ForeignKey(
        "Section", related_name="item", on_delete=models.CASCADE
    )

    def __str__(self):
        """Function for str."""
        return "{}<{}>".format(str(self.name), str(self.id))


class Modifiers(models.Model):
    """This class is used to store details for modifiers."""

    description = models.TextField()
    item = models.ManyToManyField(
        "Item", related_name='modifiers', blank=True
    )

    def __str__(self):
        """Function for str."""
        return str(self.id)