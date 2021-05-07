from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Banner(models.Model):
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return str(self.id)


class Brand(models.Model):
    title = models.CharField(max_length=120, unique=True, null=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        image = Image.open(self.img)
        (width, height) = image.size
        size = (400, 400)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.img.path)


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=120, unique=True)
    parent_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=120, unique=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Campaign(models.Model):
    campaign_slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=120, unique=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Offer(models.Model):
    offer_slug = models.SlugField(unique=True, null=True)
    offer_title = models.CharField(max_length=120, unique=True)
    offer_img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.offer_title


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    img = models.ImageField(upload_to="images/")
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, null=True)
    isFavorite = models.BooleanField()
    market_price = models.IntegerField()
    sale_price = models.IntegerField(null=True, blank=True)
    stock_quantity = models.IntegerField()
    flash_sale_offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True)
    campaign_offer = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.slug

    def save(self):
        super().save()

        image = Image.open(self.img)
        (width, height) = image.size
        size = (800, 600)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.img.path)





class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return f"productID={self.product.id}user={self.user.username}|isFavorite={self.isFavorite}"


class Currency(models.Model):
    currency_name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.currency_name
