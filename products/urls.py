from django.urls import path

from products.views import ProductListView, products_detail_view

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', products_detail_view, name='detail'),
]
