from typing import ClassVar
from .models import Users
from .forms import ClientForm
from .forms import EmployeeForm
from django.core.paginator import Paginator

from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
 

class Clients_all(ListView):
    model=Users
    template_name='users/clients.html'
    context_object_name='client'
    queryset=Users().get_clients()
    
    def get_context_data(self, **kwargs):
            ctx = super(Clients_all, self).get_context_data(**kwargs)
            client = Users().get_clients()
          

    ###################filters##########################
            
            price1 = self.request.GET.get('price1', '')
            if price1 != '' and price1 is not None :
                client = client.filter(price__gte = price1)
                ctx['price1'] = int(price1)
            
            price2 = self.request.GET.get('price2', '')
            if price2 != '' and price2 is not None :
                client = client.filter(price__lte = price2)
                ctx['price2'] = int(price2)

    ###################search##########################

            search = self.request.GET.get('id', '')
            if search != '' and search is not None:
                client = client.filter(id__icontains = search)

            search = self.request.GET.get('client', '')
            if search != '' and search is not None:
                client = client.filter(client__icontains = search)
    ###################sorting##########################

            sort = self.request.GET.get('sort', '')
            if sort != '' and sort is not None :
                client = client.client_by(sort)


            count = self.request.GET.get('count', 2)
            paginator = Paginator(client, count)
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
            ctx['client'] = page
            ctx['is_paginated'] = is_paginated
            ctx['prev' ]= prev 
            ctx['next'] = next
            ctx['count'] = int(count)
            ctx['query'] = '&sort=' + sort + '&search=' + search + '&price1=' + price1 + '&price2=' + price2
                
            
            print(ctx)
            return ctx    

 
class Client_info(DetailView):
    model=Users
    template_name='users/card_client.html'
    context_object_name='client'


    
class Client_add(CreateView):
   
    form_class = ClientForm 
    template_name='users/add_client.html'
 
    context_object_name='client'
    def post(self, request):

        form=ClientForm(request.POST)
        print(form)
        if form.is_valid():
            cl=Users()
            cl=Users.add_cl(cl,request)
        return redirect('clients')


class Client_change(UpdateView):
    model=Users
    form_class = ClientForm 
    template_name='users/change_client.html'
 
    context_object_name='client'
    def post(self, request,pk):

        form=ClientForm(request.POST)
        print(form)
        if form.is_valid():
            cl=Users()
            cl=Users.cl_change(cl,request,pk)
        return redirect('client_info',pk)

class User_delete(DeleteView):
    # model=Users
    # template_name='users/delete.html'
 
    # context_object_name='client'
    def post(self, request,pk):
        user=Users()
        user=Users.user_delete(user,request,pk)
        if (user.position==None):
            return redirect('clients')
        else:
            return redirect('employees')












def employees(request):
    return render(request, 'users/employees.html')

class Employees_all(ListView):
    model=Users
    template_name='users/employees.html'
    context_object_name='employee'
    queryset=Users().get_employees()
    def get_context_data(self, **kwargs):
            ctx = super(Employees_all, self).get_context_data(**kwargs)
            employee = Users().get_employees()
          

    ###################filters##########################
            
            price1 = self.request.GET.get('price1', '')
            if price1 != '' and price1 is not None :
                employee = employee.filter(price__gte = price1)
                ctx['price1'] = int(price1)
            
            price2 = self.request.GET.get('price2', '')
            if price2 != '' and price2 is not None :
                employee = employee.filter(price__lte = price2)
                ctx['price2'] = int(price2)

    ###################search##########################

            search = self.request.GET.get('id', '')
            if search != '' and search is not None:
                employee = employee.filter(id__icontains = search)

            search = self.request.GET.get('client', '')
            if search != '' and search is not None:
                employee = employee.filter(client__icontains = search)
    ###################sorting##########################

            sort = self.request.GET.get('sort', '')
            if sort != '' and sort is not None :
                employee = employee.client_by(sort)


            count = self.request.GET.get('count', 2)
            paginator = Paginator(employee, count)
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
            ctx['employee'] = page
            ctx['is_paginated'] = is_paginated
            ctx['prev' ]= prev 
            ctx['next'] = next
            ctx['count'] = int(count)
            ctx['query'] = '&sort=' + sort + '&search=' + search + '&price1=' + price1 + '&price2=' + price2
                
            
            print(ctx)
            return ctx    
   

class Employee_info(DetailView):
    model=Users
    template_name='users/card_employee.html'
    context_object_name='employee'

class Employee_add(CreateView):
   
    form_class = EmployeeForm 
    template_name='users/add_employee.html'
    employee_ob=Users()
    context_object_name='employee'
    def post(self, request):

        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            em=Users()
            em=Users.add_cl(em,request)
        return redirect('employees')

    def get_context_data(self,**kwargs):
        context=super(Employee_add,self).get_context_data(**kwargs)
        context['employee_ob']=self.employee_ob
        return context

class Employee_change(UpdateView):
    model=Users
    form_class = EmployeeForm 
    template_name='users/change_employee.html'
 
    context_object_name='employee'
    def post(self, request,pk):

        form=EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            em=Users()
            em=Users.em_change(em,request,pk)
        return redirect('employee_info',pk)
