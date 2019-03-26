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
    user_role = models.CharField(max_length = 100, default="Funcionario")



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


class TutorialCategory(models.Model):

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category




class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series





class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=django.utils.timezone.now())
	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title