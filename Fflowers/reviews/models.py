from django.db import models

# Create your models here.

class Reviews(models.Model):
    catalog_r = models.ForeignKey('catalog.Catalog',null=True,blank=True, related_name='catalog_r',on_delete=models.CASCADE )
    review_text = models.CharField('Текст', max_length=400,null=True,blank=True)
    name_client = models.CharField('Имя', max_length=400,null=True,blank=True)
    data = models.DateField('Дата',null=True,blank=True)
    photo = models.FileField(upload_to='static/main/image',null=True,blank=True)
    data_delete = models.DateField('Дата удаления',null=True,blank=True)


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        managed=True