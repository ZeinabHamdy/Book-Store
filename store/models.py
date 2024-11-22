from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'  # Singular name
        verbose_name_plural = 'Categories'  # Plural name


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.00),
        ],
    )
    discount = models.DecimalField(
        # 0% -> 100%
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0),
        ],
    )
    rate = models.DecimalField(
        # 0:5
        max_digits=3,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0),
        ],
    )
    image = models.ImageField(
        upload_to="images/book_images/%y/%m/%d",
        null=False,
        blank=False,
    )
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
