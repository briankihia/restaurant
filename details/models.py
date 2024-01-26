from django.db import models
from django.core.validators import MaxValueValidator

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
    

# this is the part where I set Employees duties
class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100, default='John Doe')  # Replace with your default name
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, default='N/A')  # Replace with your default phone number
    position = models.CharField(max_length=50, default='Employee')  # Replace with your default position
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')  # Replace with your default gender
    hire_date = models.DateField(default='2000-01-01')  # Replace with your default hire date
    # duty = models.CharField(max_length=100, default='No Duty Assigned')  # Replace with your default duty
    
    # the below part is used to show how to name this in the admin page
    def __str__(self):
        return self.name
# same as above,setting employees duties
class DailyDuty(models.Model):
    day = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    duty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.employee.name} - {self.duty}"



class Reservation(models.Model):
        customer_name = models.CharField(max_length=100)
#     #         # email = models.CharField(max_length=200, null=True, unique=True)  # Uncomment this line
#     #         # phone_number = models.CharField(max_length=15, blank=True, null=True, default='N/A')
#     #         # max_guests = 10  # Change this to your desired maximum number of guests
#     #         # number_of_guests = models.PositiveIntegerField(validators=[MaxValueValidator(max_guests)], default='1')
#     #         # special_request = models.TextField(blank=True, null=True)
        reservation_date = models.DateField()

        def __str__(self):
            return f"{self.customer_name} - {self.reservation_date}"
