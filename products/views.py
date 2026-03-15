from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product, ProductCategory, ProductTag, ProductColor, Manufacture, ProductStatus


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        products = Product.objects.filter(is_active=True, status=ProductStatus.AVAILABLE).order_by('-id')
        categories = self.request.GET.getlist('cat')
        tags = self.request.GET.getlist('tag')
        manufactures = self.request.GET.getlist('manufacture')
        colors = self.request.GET.getlist('color')

        categories_id_list = []
        tags_id_list = []
        manufactures_id_list = []
        colors_id_list = []

        if categories:
            categories_id_list = list(map(int, categories[0].split(',')))
        if tags:
            tags_id_list = list(map(int, tags[0].split(',')))
        if manufactures:
            manufactures_id_list = list(map(int, manufactures[0].split(',')))

        if colors:
            colors_id_list = list(map(int, colors[0].split(',')))

        if categories_id_list:
            products = products.filter(categories__id__in=categories_id_list)

        if tags_id_list:
            products = products.filter(tags__id__in=tags_id_list)

        if manufactures_id_list:
            products = products.filter(manufactures__id__in=manufactures_id_list)

        if colors_id_list:
            products = products.filter(colors__id__in=colors_id_list)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.filter(is_active=True, parent=None).order_by('-id')
        context['tags'] = ProductTag.objects.all().order_by('-id')
        context['colors'] = ProductColor.objects.all().order_by('-id')
        context['manufactures'] = Manufacture.objects.filter(is_active=True).order_by('-id')
        return context


def products_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk, is_active=True)
    except Product.DoesNotExist:
        return render(request, 'shared/404.html')

    context = {
        "product": product
    }
    return render(request,
                  'products/product-detail.html',
                  context=context
                  )


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'products'
