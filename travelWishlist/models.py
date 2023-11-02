from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

# get the length of the model
# get if its true or false if you visted a place
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, visited? {self.visited}'