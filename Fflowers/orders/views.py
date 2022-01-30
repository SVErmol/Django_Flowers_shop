from django.shortcuts import render,redirect
from .models import Orders
from .forms import OrdersForm
from django.db.models import Sum
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator

# Create your views here.

class Orders_all(ListView):
    model=Orders
    template_name='orders/orders.html'
    context_object_name='order'
    queryset=Orders().get_orders()
    def get_context_data(self, **kwargs):
            ctx = super(Orders_all, self).get_context_data(**kwargs)
            order = Orders().get_orders()
          

    ###################filters##########################
            
            price1 = self.request.GET.get('price1', '')
            if price1 != '' and price1 is not None :
                order = order.filter(price__gte = price1)
                ctx['price1'] = int(price1)
            
            price2 = self.request.GET.get('price2', '')
            if price2 != '' and price2 is not None :
                order = order.filter(price__lte = price2)
                ctx['price2'] = int(price2)

    ###################search##########################

            search = self.request.GET.get('id', '')
            if search != '' and search is not None:
                order = order.filter(id__icontains = search)

            search = self.request.GET.get('client', '')
            if search != '' and search is not None:
                order = order.filter(client__icontains = search)
    ###################sorting##########################

            sort = self.request.GET.get('sort', '')
            if sort != '' and sort is not None :
                order = order.order_by(sort)


            count = self.request.GET.get('count', 2)
            paginator = Paginator(order, count)
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
            # ctx['js'] = js
            ctx['order'] = page
            ctx['is_paginated'] = is_paginated
            ctx['prev' ]= prev 
            ctx['next'] = next
            ctx['count'] = int(count)
            ctx['query'] = '&sort=' + sort + '&search=' + search + '&price1=' + price1 + '&price2=' + price2
                
            
            print(ctx)
            return ctx    

class Orders_all_p(ListView):
    model=Orders
    template_name='orders/history.html'
    context_object_name='order'
    queryset=Orders().get_orders()

class Needed(ListView):
    model=Orders
    template_name='catalog/needed.html'
    context_object_name='needed'

class Order_info(DetailView):
    model=Orders
    template_name='orders/card_order.html'
    context_object_name='order'

class Order_add(CreateView):
   
    form_class = OrdersForm 
    template_name='orders/add_order.html'
 
    context_object_name='order'
    def post(self, request):

        form=OrdersForm(request.POST)
        print(form)
        if form.is_valid():
            ord=Orders()
            ord=Orders.add_ord(ord,request)
        return redirect('orders')


class Order_change(UpdateView):
    model=Orders
    form_class = OrdersForm 
    template_name='orders/change_order.html'
 
    context_object_name='order'
    def post(self, request,pk):

        form=OrdersForm(request.POST)
        print(form)
        if form.is_valid():
            ord=Orders()
            ord=Orders.ord_change(ord,request,pk)
        return redirect('order_info',pk)