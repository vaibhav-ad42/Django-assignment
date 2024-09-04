from django.db import models

class Image(models.Model):
    source = models.URLField()
    alt_text = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alt_text

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(Image, blank=True)
    collections = models.ManyToManyField(Collection, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Variant(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_for_sale = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.title}"
