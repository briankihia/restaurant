from django.contrib import admin
# from .models import Category, Item
from .models import *

# Register your models here.

admin.site.register(Category),
admin.site.register(Item)
admin.site.register(DailyDuty)
admin.site.register(Employee)
