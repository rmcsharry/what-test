"""
This module defines the Product model.

The Product model represents a product with an id, name, description, price, and stock.
"""

from django.db import models


class Product(models.Model):
    """
    Product model representing a product with an id, name, description, price, and stock.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        """
        String representation of the Product model.
        """
        return self.name

    def __repr__(self):
        """
        Official representation of the Product model.
        """
        return (
            f"Product(id={self.id}, name='{self.name}', "
            f"description='{self.description}', price={self.price}, stock={self.stock})"
        )
