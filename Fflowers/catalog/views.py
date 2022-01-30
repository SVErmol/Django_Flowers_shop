from typing import ClassVar
from django.shortcuts import render,redirect
from .models import Catalog
from .models import Subcategory
from .models import Favorite
from .forms import ProductForm
from .forms import CatForm
from django.core.paginator import Paginator
import json
from django.core.files.storage import FileSystemStorage

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.
def catalog_home(request):
    catalog=Catalog.objects.all()
    return render(request,'catalog/catalog.html',{'catalog':catalog})

class Products_(ListView):
    model=Catalog
    template_name='catalog/catalog.html'
    context_object_name='catalog'
    queryset=Catalog().get_products()
    
    def get_context_data(self, **kwargs):
        ctx = super(Products_, self).get_context_data(**kwargs)
        product = Catalog().get_products()

        js = {}
        for x in product:
            js[x.id] = json.loads(x.photos)
 

def products(request):
    return render(request, 'catalog/a_catalog.html')

class Product_info(DetailView):
    model=Catalog
    template_name='catalog/product.html'
    context_object_name='product'
    def get_context_data(self, **kwargs):
        ctx = super(Product_info, self).get_context_data(**kwargs)
        product = Catalog.objects.get(id = self.kwargs['pk'])

        j = json.loads(product.photos)
        ctx['j'] = j
        return ctx

class Products_all(ListView):
    model=Catalog
    template_name='catalog/a_catalog.html'
    context_object_name='product'
    queryset=Catalog().get_products()
    
    def get_context_data(self, **kwargs):
        ctx = super(Products_all, self).get_context_data(**kwargs)
        product = Catalog().get_products()

        js = {}
        for x in product:
            js[x.id] = json.loads(x.photos)

###################filters##########################
        
        price1 = self.request.GET.get('price1', '')
        if price1 != '' and price1 is not None :
            product = product.filter(price__gte = price1)
            ctx['price1'] = int(price1)
        
        price2 = self.request.GET.get('price2', '')
        if price2 != '' and price2 is not None :
            product = product.filter(price__lte = price2)
            ctx['price2'] = int(price2)

###################search##########################

        search = self.request.GET.get('name', '')
        if search != '' and search is not None:
            product = product.filter(name_product__icontains = search)
###################sorting##########################

        sort = self.request.GET.get('sort', '')
        if sort != '' and sort is not None :
            product = product.order_by(sort)


        count = self.request.GET.get('count', 2)
        paginator = Paginator(product, count)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''
        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx['search_query'] = search
        ctx['sort'] = sort
        ctx['js'] = js
        ctx['product'] = page
        ctx['is_paginated'] = is_paginated
        ctx['prev' ]= prev 
        ctx['next'] = next
        ctx['count'] = int(count)
        ctx['query'] = '&sort=' + sort + '&search=' + search + '&price1=' + price1 + '&price2=' + price2
            
        
        print(ctx)
        return ctx

    

class Products_(ListView):
    model=Catalog
    template_name='catalog/catalog.html'
    context_object_name='product'
    queryset=Catalog().get_products()
    
    def get_context_data(self, **kwargs):
        ctx = super(Products_, self).get_context_data(**kwargs)
        product = Catalog().get_products()

        js = {}
        for x in product:
            js[x.id] = json.loads(x.photos)

###################filters##########################
        
     
###################sorting##########################

        sort = self.request.GET.get('sort', '')
        if sort != '' and sort is not None :
            product = product.order_by(sort)


        count = self.request.GET.get('count', 2)
        paginator = Paginator(product, count)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''
        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        
        ctx['sort'] = sort
        ctx['js'] = js
        ctx['product'] = page
        ctx['is_paginated'] = is_paginated
        ctx['prev' ]= prev 
        ctx['next'] = next
        ctx['count'] = int(count)
        ctx['query'] = '&sort=' + sort 
            
        
        print(ctx)
        return ctx





class Basket(ListView):
    model=Favorite
    template_name='catalog/basket.html'
    context_object_name='basket'
    # queryset=Catalog().get_products()

class Favorite(ListView):
    model=Favorite
    template_name='catalog/favorite.html'
    context_object_name='favorite'

  
class Product_info_ad(DetailView):
    model=Catalog
    template_name='catalog/a_product.html'
    context_object_name='product'

    def get_context_data(self, **kwargs):
        ctx = super(Product_info_ad, self).get_context_data(**kwargs)
        product = Catalog.objects.get(id = self.kwargs['pk'])

        j = json.loads(product.photos)
        ctx['j'] = j
        return ctx

class Product_add(CreateView):
   
    form_class = ProductForm 
    template_name='catalog/add_product.html'
 
    context_object_name='product'


    def post(self, request):
        print(request.FILES.getlist('photos'))
        x = FileSystemStorage(location='static/catalog')
        dict = {}
        for f in request.FILES.getlist('photos'):

            x.save(f.name, f)
            dict['/static/catalog/' + f.name] = f.name
            print(dict)

        form=ProductForm(request.POST)
        print(form)
        if form.is_valid():
            pr=Catalog()
            pr=Catalog.add_pr(pr,request, json.dumps(dict))
        return redirect('products')

class Product_change(UpdateView):
    model=Catalog
    form_class = ProductForm 
    template_name='catalog/change_product.html'
 
    context_object_name='product'
    def post(self, request,pk):

        form=ProductForm(request.POST)
        print(form)
        if form.is_valid():
            pr=Catalog()
            pr=Catalog.pr_change(pr,request,pk)
        return redirect('product_info_ad',pk)

class Category(ListView):
    model=Subcategory
    template_name='catalog/categories.html'
    context_object_name='category'


class Category_add(CreateView):
   
    model=Subcategory
    template_name='catalog/add_categories.html'
    context_object_name='categories'
    def post(self, request):

        form=CatForm(request.POST)
        print(form)
        if form.is_valid():
            cat=Subcategory()
            cat=Subcategory.add_cat(cat,request)
        return redirect('category')