from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Process, Activity, Role, Product
from Users.models import User, Organization
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Users.forms import NewUserForm
from .forms import  SwapActivityForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django import forms


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

def removeAct(request, **kwargs):
	this_act = Activity.objects.filter(pk=kwargs['pk'])[0]
	this_proc = Process.objects.filter(pk=kwargs['fk'])[0]
	this_act.process.remove(this_proc)
	return HttpResponseRedirect('/processos/ProcessDetail/'+str(kwargs['fk']))

class ActivityCreate(CreateView):
	model = Activity
	fields = ['activity_name', 'description', 'process', 'role'] 
	template_name = "processes/forms/activity_form.html"

class ActivityUpdate(UpdateView):
	model = Activity
	fields = ['activity_name', 'description', 'process', 'role'] 
	template_name = "processes/forms/activity_update_form.html"

class ActivityDelete(DeleteView):
	model = Activity
	template_name = "processes/forms/activity_confirm_delete.html"

class ActivitySwap(CreateView):
	model = Activity
	sucess_url = "/actividades"
	template_name = "processes/forms/activity_update_form.html"
	fields = ['activity_name', 'description','role', 'process'] 
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ActivitySwap, self).get_form(form_class)
		this_act = Activity.objects.filter(pk =self.kwargs['pk'])[0]
		this_proc = Process.objects.filter(pk =self.kwargs['fk'])[0]
		form.fields['activity_name'].widget = forms.TextInput(attrs={'value': this_act.activity_name})
		form.fields['description'].widget = forms.TextInput(attrs={'value': this_act.description})
		form.initial['process'] = this_proc
		all_roles = Role.objects.all()
		form.fields['role'] = forms.ModelMultipleChoiceField(queryset=all_roles)
		roles = Role.objects.filter(pk__in = this_act.role.all())
		form.initial['role'] = roles
		
		return form   

class ProcessCreate(CreateView):
	model = Process
	fields = ['process_name', 'user' , 'description']
	template_name = "processes/forms/process_form.html"
	
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ProcessCreate, self).get_form(form_class)
		form.fields['user'].widget = forms.TextInput(attrs={'value': self.request.user, 'readonly' : "readonly"})
		return form 

class ProcessUpdate(UpdateView):
	model = Process
	fields = ['process_name', 'user' , 'description']
	template_name = "processes/forms/process_update_form.html"

class ProcessDelete(DeleteView):
	model = Process
	sucess_url = "/processos"
	template_name = "processes/forms/process_confirm_delete.html"

class ProcessDetail(DetailView):
	model = Process
	template_name = "processes/forms/process_detail.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		proc_id = self.object.id
		context['pid'] = self.kwargs['pk']
		context['proc_acts'] = Activity.objects.all().filter(process__id=proc_id)
		context['all_acts'] = Activity.objects.all()
		return context

@login_required(login_url='/login2')
def produtos(request):
	return render(request=request,
					template_name="processes/produtos.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "prods" : Product.objects.all() })




class ProductCreate(CreateView):
	model = Product
	fields = ['product_name', 'product_format', 'activity']
	template_name = "processes/forms/product_form.html"

class ProductUpdate(UpdateView):
	model = Product
	fields = ['product_name', 'product_format', 'activity']
	template_name = "processes/forms/product_update_form.html"

class ProductDelete(DeleteView):
	model = Product
	sucess_url = "/produtos"
	template_name = "processes/forms/product_confirm_delete.html"



class RoleCreate(CreateView):
	model = Role
	fields = ['role_name' , 'description', 'product']
	template_name = "processes/forms/role_form.html"

class RoleUpdate(UpdateView):
	model = Role
	fields = ['role_name' , 'description', 'product']
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
	





