from django.db import models
from django.contrib.admin.sites import NotRegistered

# Create your models here.
class Purveyors(models.Model):

    name = models.CharField('Название', max_length=400,null=True,blank=True)

    address = models.CharField('Адрес', max_length=400,null=True,blank=True)

    data_delete = models.DateField('Дата удаления',null=True,blank=True)


    
    def get_purveyors(request):
        return Purveyors.objects.filter(data_delete=None)