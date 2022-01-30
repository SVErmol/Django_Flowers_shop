
from django.db import models
from django.contrib.admin.sites import NotRegistered
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Favorite(models.Model):
    productfav = models.ForeignKey('Catalog',null=True,blank=True, related_name='productfav',on_delete=models.CASCADE )
    person = models.ForeignKey('users.Users',null=True,blank=True, related_name='person',on_delete=models.CASCADE )
    data_delete = models.DateField('Дата удаления',null=True,blank=True)



class Subcategory(models.Model):
    
    
    name = models.CharField('Название', max_length=400,null=True,blank=True)




    def add_cat(cat,request):
        cat.name=request.POST.get('name')
       

        cat.save()
        return cat

class Catalog(models.Model):
   

    subcategory = models.ForeignKey('Subcategory',null=True,blank=True, related_name='subcategory',on_delete=models.CASCADE )
    name_product = models.CharField('Название', max_length=400,null=True,blank=True)
    price = models.IntegerField('Цена', null=True,blank=True)
    purveyor = models.ForeignKey('purveyors.Purveyors',null=True,blank=True, related_name='purveyor',on_delete=models.CASCADE )
    # photo = models.FileField(upload_to='static/cataliog/',null=True,blank=True)
    photos = models.JSONField('Фотографии', default="{}")
    show = models.BooleanField(null=True,blank=True)
    data_delete = models.DateField('Дата удаления',null=True,blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Каталог'
        managed=True

# Create your models here.
    def get_products(request):
        return Catalog.objects.filter(data_delete=None)

    def add_pr(pr,request, json):
        pr.subcategory_id=request.POST.get('subcategory_id')
        pr.name_product=request.POST.get('name_product')
        pr.price=request.POST.get('price')
        pr.suplier_id=request.POST.get('suplier_id')
        pr.photos=json
        pr.show=request.POST.get('show')

        pr.save()
        return pr

    def pr_change(pr,request,pk):
        pr=Catalog.objects.get(id=pk)
        pr.subcategory_id=request.POST.get('subcategory_id')
        pr.name_product=request.POST.get('name_product')
        pr.price=request.POST.get('price')
        pr.suplier_id=request.POST.get('suplier_id')
        pr.photo=request.POST.get('photo')
        pr.show=request.POST.get('show')

        pr.save()
        return pr