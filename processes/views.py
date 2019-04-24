from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import  Process, Activity, Role, Product
from Users.models import User, Organization
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Users.forms import NewUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView



def gparea(request):
	return render(request=request,
				  template_name="processes/gparea.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})

@login_required(login_url='/login2')
def processos(request):
	return render(request=request,
				  template_name="processes/processos.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})


@login_required(login_url='/login2')
def actividades(request):
	return render(request=request,
				  template_name="processes/actividades.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})

class ActivityCreate(CreateView):
	model = Activity
	fields = ['activity_name', 'description', 'process'] 
	template_name = "processes/forms/activity_form.html"

class ActivityUpdate(UpdateView):
	model = Activity
	fields = ['activity_name', 'description', 'process'] 
	template_name = "processes/forms/activity_update_form.html"

class ActivityDelete(DeleteView):
	model = Activity
	template_name = "processes/forms/activity_confirm_delete.html"



class ProcessCreate(CreateView):
	model = Process
	fields = ['process_name', 'description', 'user' ]
	template_name = "processes/forms/process_form.html"

class ProcessUpdate(UpdateView):
	model = Process
	fields = ['process_name', 'description', 'user' ]
	template_name = "processes/forms/process_update_form.html"

class ProcessDelete(DeleteView):
	model = Process
	sucess_url = "/processos"
	template_name = "processes/forms/process_confirm_delete.html"


@login_required(login_url='/login2')
def produtos(request):
	return render(request=request,
					template_name="processes/produtos.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "prods" : Product.objects.all() })




class ProductCreate(CreateView):
	model = Product
	fields = ['product_name', 'product_format']
	template_name = "processes/forms/product_form.html"

class ProductUpdate(UpdateView):
	model = Product
	fields = ['product_name', 'product_format']
	template_name = "processes/forms/product_update_form.html"

class ProductDelete(DeleteView):
	model = Product
	sucess_url = "/produtos"
	template_name = "processes/forms/product_confirm_delete.html"

class RoleCreate(CreateView):
	model = Role
	fields = ['role_name' , 'description', 'activity']
	template_name = "processes/forms/role_form.html"

class RoleUpdate(UpdateView):
	model = Role
	fields = ['role_name' , 'description', 'activity']
	template_name = "processes/forms/role_update_form.html"

class RoleDelete(DeleteView):
	model = Role
	sucess_url = "/papeis"
	template_name = "processes/forms/role_confirm_delete.html"


@login_required(login_url='/login2')
def home(request):
	return render(request=request,
				  template_name="processes/homepage.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all(),
				   			"roles": Role.objects.all()	, "users" : User.objects.all(),	
							 "orgs" : Organization.objects.all(), "prods" : Product.objects.all(),							

				   }
				   )

@login_required(login_url='/login2')
def papeis(request):
	return render(request=request,
				  template_name="processes/papeis.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all(),
				   			"roles": Role.objects.all()	, "users" : User.objects.all(),	
							  "prods" : Product.objects.all(),							
				   }
				   )
	





