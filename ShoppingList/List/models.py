from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=200)
    cost = models.IntegerField()
    quantity = models.IntegerField()
 
    def __str__(self):
        return self.item
