from django.shortcuts import render
from .models import *
from django.http import JsonResponse

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

    return JsonResponse(product_data,safe=False)

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

    return JsonResponse(variant_data,safe=False)

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

    return JsonResponse(collection_data,safe=False)

def products_by_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    products = collection.product_set.all()
    product_data = [
        {
            "title": product.title,
            "description": product.description,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "images": [image.source.url for image in product.images.all()],
        } 
        for product in products
    ]
    return JsonResponse(product_data,safe=False)

def variants_by_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    variants = Variant.objects.filter(product__collections=collection)
    variant_data = [
        {
            "title": f"{variant.product.title} - {variant.title}",
            "created_at": variant.created_at,
            "updated_at": variant.updated_at,
            "available_for_sale": variant.available_for_sale,
            "price": variant.price,
            "image": variant.image.source.url,
        } 
        for variant in variants
    ]
    return JsonResponse(variant_data,safe=False)

def variants_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    variants = Variant.objects.filter(product__category=category)
    variant_data = [
        {
            "title": f"{variant.product.title} - {variant.title}",
            "created_at": variant.created_at,
            "updated_at": variant.updated_at,
            "available_for_sale": variant.available_for_sale,
            "price": variant.price,
            "image": variant.image.source.url,
        } 
        for variant in variants
    ]
    return JsonResponse(variant_data,safe=False)