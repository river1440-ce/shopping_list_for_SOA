from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Item(models.Model):
    """Model representing a item."""
    title = models.CharField(max_length=200)
    amount = models.IntegerField(help_text='Enter what amount of this item would you like to buy.')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the item.')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this item."""
        return reverse('item-detail', args=[str(self.id)])

    class Meta:
        permissions = (("can_read_all_item", "can_change_all_item"),)
