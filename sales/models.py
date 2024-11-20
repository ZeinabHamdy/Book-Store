from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


def validatePassword(value):
    if len(value) < 8 :
        raise ValidationError('Password must be at least 8 characters.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('Password must contain at least one digit.')
    if not any(char.isalpha() for char in value):
        raise ValidationError('Password must contain at least one letter.')

def validateUsername(value):
    for ch in value :
        if ch.isalpha() or ch =='_' or ch.isdigit():
            continue
        else:
            raise ValidationError('username should be alpha/digit/_ values only.')


def validatePhone(value):
    if value[0] !='+' and not value[0].isdigit():
        raise ValidationError('that is not a phone number!')

    for idx in range(1,len(value)) :
        if not value[idx].isdigit():
            raise ValidationError('that is not a phone number!')



class Customer(models.Model):
    username = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
        validators=[
            validateUsername
        ],
    )
    email = models.EmailField(
        unique=True,
    )
    phone = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        validators=[
            validatePhone
        ],
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        validators=[
            validatePassword
        ],
    )
    address = models.TextField(
        max_length=200,
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.username





class Order(models.Model):
    status = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=[
            ('pending' , 'pending'),
            ('delivered','delivered'),
            ('canceled','canceled')
        ],
    )
    total_price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.00),
        ],
    )
    order_date=models.DateTimeField(
        null=False,
        blank=False,
    )
    sent_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=False,
    )

    def __str__(self):
        return f"Customer : {self.customer.username} Order : {self.id}"


class Item(models.Model):
    quantity=models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),
        ],
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null =False,
    )

    book = models.ForeignKey(
        'store.Book',
        on_delete=models.CASCADE,
        null=False,
    )

    @property
    def total_price(self):
        return self.quantity * self.book.price if self.quantity else 0

