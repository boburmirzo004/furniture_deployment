from django.urls import path

from products.views import ProductListView, products_detail_view, add_or_remove_like_from_wishlist, \
    add_or_remove_from_cart

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', products_detail_view, name='detail'),
    path('<int:pk>/wishlist', add_or_remove_like_from_wishlist, name='wishlist'),
    path('<int:pk>/cart', add_or_remove_from_cart, name='cart'),
]
