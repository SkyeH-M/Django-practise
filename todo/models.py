from django.db import models

# Create your models here.
# if you need functionality from 1 class to be available in another
# you need to inherit the one you need
class Item(models.Model):
    # Django will create id field automatically
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
# takes in class itself as its argument
    def __str__(self):
        return self.name

