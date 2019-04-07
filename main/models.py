import django
from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.





class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
            permissions =( ("can_do", "Permission to do stuff"),)
             

    
class User(AbstractUser):
    id = models.AutoField(db_column='ID',primary_key=True)
    username = models.CharField(db_column='UserName',
                                max_length=255,
                                unique=True,
                                blank=True,
                                null=True)
    useremail = models.CharField(db_column='UserEmail',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    password = models.CharField(db_column='Password',
                                max_length=255,
                                blank=True,null=True)


    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)




    class Meta:
        managed = True
        db_table = 'User'
        permissions = ( 
            ("test_GProc", "Teste de permissao geral Gestor de Processos"), 
            ("test_Analist", "Teste de permissao geral Analista"), 
            ("test_Func", "Teste de permissao geral Funcionário"), 
            ("test_Admin", "Teste de permissao geral Administrador"),)
       




class Process(models.Model):
        process_name = models.CharField(max_length=200)
        user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
        creation_date = models.DateTimeField("date created", default=django.utils.timezone.now())
        description = models.TextField(max_length=200)

        def __str__(self):
            return self.process_name

class Activity(models.Model):
        activity_name = models.CharField(max_length=200)
        process = models.ForeignKey(Process,  null=True, blank=True,on_delete=models.SET_NULL)
        description = models.TextField(max_length=200)

        def __str__(self):
            return self.activity_name

class Role(models.Model):
        role_name = models.CharField(max_length=200)
        activity = models.ForeignKey(Activity,  null=True, blank=True,on_delete=models.SET_NULL)
        description = models.TextField(max_length=200)

        def __str__(self):
            return self.role_name



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=1)
    product_format = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_name

