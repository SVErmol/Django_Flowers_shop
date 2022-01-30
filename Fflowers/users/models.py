from datetime import date
from django.contrib.admin.sites import NotRegistered
from django.db import models
from django.db.models import Q
# Create your models here.
class Users(models.Model):
    pos_em=[
        (1,'Администратор'),
        (2,'Флорист'),
        (3,'Курьер')
    ]

    surname = models.CharField('Фамилия', max_length=400,null=True,blank=True)
    name = models.CharField('Имя', max_length=400,null=True,blank=True)
    patronymic = models.CharField('Отчество', max_length=400,null=True,blank=True)
    position = models.IntegerField('Должность',null=True,blank=True,choices=pos_em,default=None)

    birthday = models.DateField('Дата рождения',null=True,blank=True)
    phone = models.CharField('Номер', max_length=15,null=True,blank=True)
    note = models.TextField('Комментарий',null=True,blank=True)
    email = models.EmailField('Почта',null=True,blank=True)
    password = models.CharField('Пароль', max_length=100,null=True,blank=True)
    data_delete = models.DateField('Дата удаления',null=True,blank=True)

    def add_cl(cl,request):
        cl.surname=request.POST.get('surname')
        cl.name=request.POST.get('name')
        cl.patronymic=request.POST.get('patronymic')
        cl.birthday=request.POST.get('birthday')
        cl.phone=request.POST.get('phone')
        cl.note=request.POST.get('note')
        cl.email=request.POST.get('email')

        cl.save()
        return cl

    def cl_change(cl,request,pk):
        cl=Users.objects.get(id=pk)
        cl.surname=request.POST.get('surname')
        cl.name=request.POST.get('name')
        cl.patronymic=request.POST.get('patronymic')
        cl.birthday=request.POST.get('birthday')
        cl.phone=request.POST.get('phone')
        cl.note=request.POST.get('note')
        cl.email=request.POST.get('email')

        cl.save()
        return cl

    def user_delete(user,request,pk):
        user=Users.objects.get(id=pk)
        user.data_delete=date.today()
        user.save()
        return user


    def get_clients(request):
        return Users.objects.filter(data_delete=None, position=None)
    
    def get_employees(request):
        return Users.objects.filter(Q(data_delete=None) & (Q(position = 1) | Q(position = 2)| Q(position = 3)))




    def add_em(em,request):
        em.surname=request.POST.get('surname')  
        em.name=request.POST.get('name')
        em.patronymic=request.POST.get('patronymic')
        em.birthday=request.POST.get('birthday')
        em.phone=request.POST.get('phone')
        em.note=request.POST.get('note')
        em.email=request.POST.get('email')

        em.save()
        return em

    def em_change(em,request,pk):
        em=Users.objects.get(id=pk)
        em.surname=request.POST.get('surname')
        em.name=request.POST.get('name')
        em.patronymic=request.POST.get('patronymic')
        em.birthday=request.POST.get('birthday')
        em.phone=request.POST.get('phone')
        em.note=request.POST.get('note')
        em.email=request.POST.get('email')

        em.save()
        return em

 