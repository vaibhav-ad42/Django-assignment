from django.shortcuts import render
from .models import *

def list_products(request):
    products=Product.objects.all()
    product_data=[
        {
            "title":product.title,
            "description":product.description,
            "created_at":product.created_at,
            "updated_at":product.updated_at,
            "images": [image.source.url for image in product.images.all()]
        }
        for product in products
    ]

    return render(request,'store/product_list.html',{'products':product_data})

def list_variants(request):
    variants=Variant.objects.all()
    variant_data=[
        {
            "title":f"{variant.product.title}-{variant.title}",
            "created_at":variant.created_at,
            "updated_at":variant.updated_at,
            "available_sale":variant.available_sale,
            "price":variant.price,
            "image": variant.image.source.url,
        }
        for variant in variants
    ]

    return render(request,'store/variant_list.html',{'variants':variant_data})

def list_collections(request):
    collections=Collection.objects.all()
    collection_data=[
        {
            "title":collection.title,
            "published":collection.published,
            "updated_at":collection.updated_at,
        }
        for collection in collections
    ]

    return render(request,'store/collections_list.html',{'collections':collection_data})

