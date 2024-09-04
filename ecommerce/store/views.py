from django.http import JsonResponse
from .models import Product, Variant, Collection, Category

def list_products(request):
    products = Product.objects.all()
    data = [
        {
            "Title": product.title,
            "Description": product.description,
            "Created_at": product.created_at,
            "Updated_at": product.updated_at,
            "Images": [{"source": img.source, "alt_text": img.alt_text} for img in product.images.all()]
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def list_variants(request):
    variants = Variant.objects.all()
    data = [
        {
            "Title": f"{variant.product.title} - {variant.title}",
            "Created_at": variant.created_at,
            "Updated_at": variant.updated_at,
            "Available_for_sale": variant.available_for_sale,
            "Price": variant.price,
            "Image": {
                "source": variant.image.source,
                "alt_text": variant.image.alt_text
            }
        }
        for variant in variants
    ]
    return JsonResponse(data, safe=False)

def list_collections(request):
    collections = Collection.objects.all()
    data = [
        {
            "Title": collection.title,
            "Published": collection.published,
            "Updated_at": collection.updated_at,
        }
        for collection in collections
    ]
    return JsonResponse(data, safe=False)

def list_products_by_collections(request, collection_ids):
    collections = Collection.objects.filter(id__in=collection_ids)
    products = Product.objects.filter(collections__in=collections).distinct()
    data = [
        {
            "Title": product.title,
            "Description": product.description,
            "Created_at": product.created_at,
            "Updated_at": product.updated_at,
            "Images": [{"source": img.source, "alt_text": img.alt_text} for img in product.images.all()]
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def list_variants_by_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    products = collection.product_set.all()
    variants = Variant.objects.filter(product__in=products)
    data = [
        {
            "Title": f"{variant.product.title} - {variant.title}",
            "Created_at": variant.created_at,
            "Updated_at": variant.updated_at,
            "Available_for_sale": variant.available_for_sale,
            "Price": variant.price,
            "Image": {
                "source": variant.image.source,
                "alt_text": variant.image.alt_text
            }
        }
        for variant in variants
    ]
    return JsonResponse(data, safe=False)

def list_variants_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    variants = Variant.objects.filter(product__in=products)
    data = [
        {
            "Title": f"{variant.product.title} - {variant.title}",
            "Created_at": variant.created_at,
            "Updated_at": variant.updated_at,
            "Available_for_sale": variant.available_for_sale,
            "Price": variant.price,
            "Image": {
                "source": variant.image.source,
                "alt_text": variant.image.alt_text
            }
        }
        for variant in variants
    ]
    return JsonResponse(data, safe=False)
