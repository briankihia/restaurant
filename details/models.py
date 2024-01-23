from django.db import models

# To create a Django model for your restaurant website where owners can update an appetizer page, main dish page, and dessert page, you can define three models—one for each section. Below is an example of how your models.py file could be structured:

#     Category: Represents the category of the menu items (e.g., "Appetizers," "Main Dishes," "Desserts"). You can add more fields to this model if needed, such as a description or image.
# Item: Represents the individual menu items. It has a foreign key to Category to link each item to a specific category. The description field can contain details about the item, and the price field stores the item's price. The image field is optional and can be used to store an image of the item.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    items= models.ManyToManyField(Item)
    