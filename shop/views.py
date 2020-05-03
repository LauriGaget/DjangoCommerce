from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Category
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from users.models import UserCustom
# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        simular_products = products.filter(category=self.object.category)

        context['categories'] = Category.objects.all()
        context['simular_products'] = simular_products

        return context


class ProductListView(ListView):
    model = Product
    template_name = "shop/product_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def product_category_list(request, category_slug=None):

    categories = Category.objects.all()
    products = Product.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    product_list = products.filter(category=category)
    return render(request,
                  'shop/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'product_list': product_list})


def add_to_favori(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    user = UserCustom.objects.get(id=user_id)
    user.favori.add(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def delete_from_favori(request, product_id, user_id):
    product = Product.objects.get(id=product_id)
    user = UserCustom.objects.get(id=user_id)
    user.favori.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

