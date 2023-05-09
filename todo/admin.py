from django.contrib import admin
# from current directories models file, import Item class
from .models import Item

# Register your models here.
admin.site.register(Item)