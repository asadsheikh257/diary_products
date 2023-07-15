from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('CR','CRUD'),
    ('ML','MILK'),
    ('LS','LASSI'),
    ('MS','MILKSHAKE'),
    ('PN','PANEER'),
    ('GH','GHEE'),
    ('CZ','CHEESE'),
    ('IC','ICECREAM'),  
)

STATE_CHOICES = (
    ('PUNJAB','PUNJAB'),
    ('SINDH','SINDH'),
    ('BALOCHISTAN','BALOCHISTAN'),
    ('KPK','KHAIBAR PAKHTOONKHAWA'),
    ('GILGIT BALTISTAN','GILGIT BALTISTAN'),
    ('AZAD KASHMIR','AZAD KASHMIR'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self) -> str:
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return self.name
    