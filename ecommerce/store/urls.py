from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='list_products'),
    path('variants/', views.list_variants, name='list_variants'),
    path('collections/', views.list_collections, name='list_collections'),
    path('collections/<int:collection_id>/products/', views.list_products_by_collections, name='list_products_by_collections'),
    path('collections/<int:collection_id>/variants/', views.list_variants_by_collection, name='list_variants_by_collection'),
    path('categories/<int:category_id>/variants/', views.list_variants_by_category, name='list_variants_by_category'),
]
