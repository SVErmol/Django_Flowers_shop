from django.db import models

# Create your models here.
class Feedback(models.Model):
   
    admin = models.ForeignKey('users.Users',null=True,blank=True, related_name='admin',on_delete=models.CASCADE )
    dateProcessed = models.DateField('Дата обработки',null=True,blank=True)
    date = models.DateField('Дата',null=True,blank=True)
    text = models.CharField('Текст', max_length=400,null=True,blank=True)
    phone = models.CharField('Номер', max_length=15,null=True,blank=True)
    name = models.CharField('Имя', max_length=400,null=True,blank=True)


    