import django
from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User, Group

# Create your models here.






class Post(models.Model):
		title = models.CharField(max_length=200)
		body = models.TextField()
		username = models.ForeignKey(User,  on_delete="cascade")
		published = models.DateTimeField("date published", default=django.utils.timezone.now())

		def __str__(self):
			return self.title


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

class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
            permissions =( ("can_do", "Permission to do stuff"),)
             

    

class User(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")
    Organization = models.ForeignKey(Organization, default="None", on_delete=models.SET_DEFAULT)
    user_profile = models.CharField(max_length = 100, default="Funcionario")



    class Meta:
            permissions = ( 
            ("can_eat_apples", "Permission to eat apples"), 
            ("can_go_in_ac_bus", "To provide AC-Bus facility"), 
            ("can_stay_ac-room", "To provide staying at AC room"), 
            ("test_GProc", "Teste de permissao Gestor de Processos"), 
            ("test_Analist", "Teste de permissao Analista"), 
            ("test_Func", "Teste de permissao Funcionário"), 
            ("can_go_mussoorie", "Trip to Mussoorie"), 
            ("can_go_haridwaar", "Trip to Haridwaar"), 
            ("can_go_rishikesh", "Trip to Rishikesh"),)





class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=1)
    product_format = models.CharField(max_length=200)
    
    def __str__(self):
        return self.product_name

