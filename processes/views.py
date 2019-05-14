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

@login_required(login_url='/login2')
def removeActivityFromProcess(request, **kwargs):
	this_act = Activity.objects.filter(pk=kwargs['pk'])[0]
	this_proc = Process.objects.filter(pk=kwargs['fk'])[0]
	this_act.process.remove(this_proc)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#previous URL

@login_required(login_url='/login2')
def addActivityToProcess(request, **kwargs):
	this_act = Activity.objects.filter(pk=kwargs['pk'])[0]
	this_proc = Process.objects.filter(pk=kwargs['fk'])[0]
	this_act.process.add(this_proc)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class ActivityCreate(CreateView):
	model = Activity
	fields = ['activity_name', 'description', 'process', 'role'] 
	template_name = "processes/forms/activity_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ActivityCreate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['role'] = forms.ModelMultipleChoiceField(queryset=Role.objects.all() ,widget=forms.CheckboxSelectMultiple())
		form.fields['process'] = forms.ModelMultipleChoiceField(queryset=Process.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form	

class ActivityDetail(DetailView):
	model = Activity
	template_name = "processes/forms/activity_detail.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		act_id = self.object.id
		context['pid'] = self.kwargs['pk']
		our_products = Product.objects.all().filter(activity__id=act_id)
		our_procs = Process.objects.all().filter(activity__id=act_id)
		this_act = Activity.objects.all().filter(id=act_id)[0]
		our_roles = this_act.role.all()
		context['act_products'] = our_products
		context['non_products'] = Product.objects.all().exclude(id__in=our_products)
		context['procs'] = this_act.process.all()
		context['non_procs'] = Process.objects.all().exclude(id__in=our_procs)
		context['roles'] = our_roles
		context['non_roles'] = Role.objects.all().exclude(id__in=our_roles)
		return context

class ActivityUpdate(UpdateView):
	model = Activity
	fields = ['activity_name', 'description', 'process', 'role'] 
	template_name = "processes/forms/activity_update_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ActivityUpdate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['role'] = forms.ModelMultipleChoiceField(queryset=Role.objects.all() ,widget=forms.CheckboxSelectMultiple())
		form.fields['process'] = forms.ModelMultipleChoiceField(queryset=Process.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form		

class ActivityDelete(DeleteView):
	model = Activity
	template_name = "processes/forms/activity_confirm_delete.html"
	def get_context_data(self, **kwargs):
		context = super(ActivityDelete, self).get_context_data(**kwargs)
		this_act = Activity.objects.filter(pk =self.kwargs['pk'])[0]
		this_act_procs = this_act.process.all()
		context['act_procs'] = this_act_procs
		return context

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
		form.fields['process'] = forms.ModelMultipleChoiceField(queryset=Process.objects.all() ,widget=forms.CheckboxSelectMultiple())
		form.initial['process'] = this_proc
		all_roles = Role.objects.all()
		form.fields['role'] = forms.ModelMultipleChoiceField(queryset=all_roles, widget=forms.CheckboxSelectMultiple())
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
		#form.fields['user'].widget = forms.TextInput(attrs={'value': self.request.user, 'readonly' : "readonly"})
		form.initial['user'] = self.request.user
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
		our_acts = Activity.objects.all().filter(process__id=proc_id)
		context['proc_acts'] = our_acts
		context['non_acts'] = Activity.objects.all().exclude(id__in=our_acts)
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
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ProductCreate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['activity'] = forms.ModelMultipleChoiceField(queryset=Activity.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form

class ProductDetail(DetailView):
	model = Product
	template_name = "processes/forms/product_detail.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		product_id = self.object.id
		context['pid'] = self.kwargs['pk']
		this_product = Product.objects.all().filter(id=product_id)[0]
		our_acts = this_product.activity.all()
		our_roles = Role.objects.all().filter(product__id=product_id)
		context['acts'] = our_acts
		context['non_acts'] = Activity.objects.all().exclude(id__in=our_acts)
		context['roles'] = our_roles
		context['non_roles'] = Role.objects.all().exclude(id__in=our_roles)
		return context


class ProductUpdate(UpdateView):
	model = Product
	fields = ['product_name', 'product_format', 'activity']
	template_name = "processes/forms/product_update_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(ProductUpdate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['activity'] = forms.ModelMultipleChoiceField(queryset=Activity.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form


class ProductDelete(DeleteView):
	model = Product
	sucess_url = "/produtos"
	template_name = "processes/forms/product_confirm_delete.html"


@login_required(login_url='/login2')
def removeActivityFromProduct(request, **kwargs):
	this_product = Product.objects.filter(pk=kwargs['pk'])[0]
	this_act = Activity.objects.filter(pk=kwargs['fk'])[0]
	this_product.activity.remove(this_act)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#previous URL

@login_required(login_url='/login2')
def addActivityToProduct(request, **kwargs):
	this_product = Product.objects.filter(pk=kwargs['pk'])[0]
	this_act = Activity.objects.filter(pk=kwargs['fk'])[0]
	this_product.activity.add(this_act)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



class RoleCreate(CreateView):
	model = Role
	fields = ['role_name' , 'description', 'product']
	template_name = "processes/forms/role_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(RoleCreate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['product'] = forms.ModelMultipleChoiceField(queryset=Product.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form

class RoleDetail(DetailView):
	model = Role
	template_name = "processes/forms/role_detail.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		role_id = self.object.id
		context['pid'] = self.kwargs['pk']
		this_rol = Role.objects.all().filter(id=role_id)[0]
		our_products = this_rol.product.all()
		our_acts = Activity.objects.all().filter(role__id=role_id)
		context['products'] = our_products
		context['non_products'] = Product.objects.all().exclude(id__in=our_products)
		context['acts'] = our_acts
		context['non_acts'] = Activity.objects.all().exclude(id__in=our_acts)
		return context


class RoleUpdate(UpdateView):
	model = Role
	fields = ['role_name' , 'description', 'product']
	template_name = "processes/forms/role_update_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(RoleUpdate, self).get_form(form_class)
		#form.fields['user'].widget
		form.fields['product'] = forms.ModelMultipleChoiceField(queryset=Product.objects.all() ,widget=forms.CheckboxSelectMultiple())
		return form
		
class RoleDelete(DeleteView):
	model = Role
	sucess_url = "/papeis"
	template_name = "processes/forms/role_confirm_delete.html"


@login_required(login_url='/login2')
def removeRoleFromActivity(request, **kwargs):
	this_act = Activity.objects.filter(pk=kwargs['pk'])[0]
	this_rol = Role.objects.filter(pk=kwargs['fk'])[0]
	this_act.role.remove(this_rol)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#previous URL

@login_required(login_url='/login2')
def addRoleToActivity(request, **kwargs):
	this_act = Activity.objects.filter(pk=kwargs['pk'])[0]
	this_rol = Role.objects.filter(pk=kwargs['fk'])[0]
	this_act.role.add(this_rol)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


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
	

@login_required(login_url='/login2')
def removeProductFromRole(request, **kwargs):
	this_product = Product.objects.filter(pk=kwargs['pk'])[0]
	this_rol = Role.objects.filter(pk=kwargs['fk'])[0]
	this_rol.product.remove(this_product)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#previous URL

@login_required(login_url='/login2')
def addProductToRole(request, **kwargs):
	this_product = Product.objects.filter(pk=kwargs['pk'])[0]
	this_rol = Role.objects.filter(pk=kwargs['fk'])[0]
	this_rol.product.add(this_product)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




