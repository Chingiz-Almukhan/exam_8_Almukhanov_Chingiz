from django.urls import path

from market.views.add_product_view import AddProductView
from market.views.add_review import AddReviewView
from market.views.base import IndexView
from market.views.delete_product_view import DeleteProductView
from market.views.delete_review import delete
from market.views.edit_product_view import EditProductView
from market.views.edit_review import EditReviewView
from market.views.product_view import ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('add/product', AddProductView.as_view(), name='add_product'),
    path('edit/product/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('delete/confirm/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),
    path('delete/review/<int:pk>', delete, name='delete_review'),
    path('edit/review/<int:pk>', EditReviewView.as_view(), name='edit_review'),
]
