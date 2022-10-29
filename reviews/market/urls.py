from django.urls import path

from market.views.add_product_view import AddProductView
from market.views.base import IndexView
from market.views.delete_product_view import DeleteProductView
from market.views.edit_product_view import EditProductView
from market.views.product_view import ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('add/product', AddProductView.as_view(), name='add_product'),
    path('edit/product/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('delete/confirm/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
    # path('projects/', ProjectView.as_view(), name='projects'),
    # path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
    # path('add/project', AddProjectView.as_view(), name='add_project'),
    # path('edit/user/<int:pk>', EditUserView.as_view(), name='edit_user'),
    # path('delete/project/<int:pk>', DeleteProjectView.as_view(), name='delete_project'),
    # path('edit/project/<int:pk>', EditProjectView.as_view(), name='edit_project')
]
