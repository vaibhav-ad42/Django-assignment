from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='product-list'),
    path('variants/',views.list_variants, name='variant-list'),
    path('collections/',views.list_collections , name='collection-list'),
    path('collections/<int:collection_id>/products/',views.products_by_collection , name='products-by-collection'),
    path('collections/<int:collection_id>/variants/', views.variants_by_collection, name='variants-by-collection'),
    path('categories/<int:category_id>/variants/',views.variants_by_category, name='variants-by-category'),
]
