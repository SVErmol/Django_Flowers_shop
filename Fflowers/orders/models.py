from django.db import models
from django.contrib.admin.sites import NotRegistered

# Create your models here.
class Orders(models.Model):
    st=[
        (1,'Обработан'),
        (2,'Доставлен')
    ]


    courier = models.ForeignKey('users.Users',null=True,blank=True, related_name='courier',on_delete=models.CASCADE )
    florist = models.ForeignKey('users.Users',null=True,blank=True, related_name='florist',on_delete=models.CASCADE )
    client = models.ForeignKey('users.Users',null=True,blank=True, related_name='client',on_delete=models.CASCADE )
    address = models.CharField('Адрес', max_length=400,null=True,blank=True)
    dateorder = models.DateField('Дата заказа',null=True,blank=True)
    datedelivery = models.DateField('Дата доставки',null=True,blank=True)
    datepay = models.DateField('Дата оплаты',null=True,blank=True)
    sum = models.CharField('Цена', max_length=200,null=True,blank=True)
    status = models.IntegerField('Статус',null=True,blank=True,choices=st,default=None)
    note = models.TextField('Комментарий',null=True,blank=True)
    data_delete = models.DateField('Дата удаления',null=True,blank=True)



    def get_orders(request):
        return Orders.objects.filter(data_delete=None)

    def add_ord(ord,request):
        ord.courier=request.POST.get('courier')
        ord.florist=request.POST.get('florist')
        ord.client=request.POST.get('client')
        ord.address=request.POST.get('address')
        ord.dateorder=request.POST.get('dateorder')
        ord.datedelivery=request.POST.get('datedelivery')
        ord.datepay=request.POST.get('datepay')
        ord.sum=request.POST.get('sum')
        ord.status=request.POST.get('status')
        ord.note=request.POST.get('note')

        ord.save()
        return ord    

    def ord_change(ord,request,pk):
        ord=Orders.objects.get(id=pk)
        ord.courier=request.POST.get('courier')
        ord.florist=request.POST.get('florist')
        ord.client=request.POST.get('client')
        ord.address=request.POST.get('address')
        ord.dateorder=request.POST.get('dateorder')
        ord.datedelivery=request.POST.get('datedelivery')
        ord.datepay=request.POST.get('datepay')
        ord.sum=request.POST.get('sum')
        ord.status=request.POST.get('status')
        ord.note=request.POST.get('note')

        ord.save()
        return ord    

class OrderContent(models.Model):
    order = models.ForeignKey('Orders',null=True,blank=True, related_name='order',on_delete=models.CASCADE )
    product = models.ForeignKey('catalog.Catalog',null=True,blank=True, related_name='product',on_delete=models.CASCADE )
    quantity  = models.CharField('Количество', max_length=200,null=True,blank=True)
