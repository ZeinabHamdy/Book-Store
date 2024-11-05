from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model) :
    title = models.CharField(
        max_length = 100,
        null = False, # default value 
        blank = False, #default value
        default = 'no title',
    )
    price = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        null = False,
        blank = False,
        default=0.0,
        validators=[MinValueValidator(0.00)],
    )
    discount = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        null = True,
        blank = True,
        validators=[MinValueValidator(0.00)],
    )
    rate = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        null = True,
        blank = True,
    )
    
    # fk author id
    # fk category id

    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
    )


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
    )


    def __str__(self):
        return self.name