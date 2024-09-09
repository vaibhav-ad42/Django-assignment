from django.contrib import admin
from .models import Product, Variant, Image, Collection, Category

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Image)
admin.site.register(Collection)
admin.site.register(Category)
