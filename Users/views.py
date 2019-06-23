from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse
from processes.models import Process, Activity, Role, Product
from .models import User, Organization
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.models import Group
from Activities.models import Pattern, Sentence
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import PasswordChangeView
from django import forms
# Create your views here.


class UserDelete(DeleteView):
	model = User
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_confirm_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['logged_user'] = self.request.user
		return context


class UserDetail(DetailView):
	model = User
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['logged_user'] = self.request.user
		context['procs'] = Process.objects.all()
		context['patts'] = Pattern.objects.filter(userid=self.object.id)
		context['sentecs'] = Sentence.objects.filter(userid=self.object.id)
		return context


class UserChangePassword(PasswordChangeView):
	model = User
	template_name = "processes/forms/user_update_pass.html"
	sucess_url = "/utilizadores"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(UserChangePassword, self).get_form(form_class)
		form.fields['old_password'].label = "Insira a password actual"
		form.fields['new_password1'].label = "Insira a password nova"
		form.fields['new_password2'].label = "Confirme a password nova"
		return form
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['this_user'] = self.kwargs["pk"]
		context['referer'] = self.request.META.get('HTTP_REFERER')
		return context



class UserCreate(CreateView):
	model = User
	form_class = NewUserForm
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(UserCreate, self).get_form(form_class)
		form.fields['organization'].empty_label = None
		form.fields['email'].error_messages = "..."
		form.fields['username'].label = "Nome de utilizador"
		form.fields['organization'].label = "Empresa"
		form.fields['group'] = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple())
		form.fields['group'].label = "Perfil"
		form.fields['password2'].help_text = "Por favor confirme a password"
		form.fields['group'].help_text = "Selecione o(s) perfil(s) do utilizador"
		form.fields['password2'].label = "Confirmar Password"
		return form 		

class UserUpdate(UpdateView):
	model = User
	fields = ['username', 'email', 'organization', 'groups']
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_update_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(UserUpdate, self).get_form(form_class)
		form.fields['organization'].empty_label = None
		form.fields['email'].error_messages = "..."
		form.fields['organization'].label = "Empresa"
		form.fields['groups'] = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple())
		form.fields['groups'].label = "Perfil"
		return form

class UserUpdateEmail(UpdateView):
	model = User
	fields = ['email']
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_update_email_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(UserUpdateEmail, self).get_form(form_class)
		form.fields['email'].label = "Introduza o novo e-mail"
		form.fields['email'].required = True
		form.fields['email'].widget = forms.EmailInput()
	
		return form
	def get_context_data(self, **kwargs):	
		context = super().get_context_data(**kwargs)
		context['referer'] = self.request.META.get('HTTP_REFERER')
		context['logged_user'] = self.request.user
		return context


class OrganizationCreate(CreateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "processes/forms/organization_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(OrganizationCreate, self).get_form(form_class)
		form.fields['name'].label = "Nome da Empresa"
		form.fields['location'].label = "Localização"
		return form


class OrganizationDetail(DetailView):
	model = Organization
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['org_users'] = User.objects.filter(organization__id =self.kwargs['pk'])
		return context
	

class OrganizationDelete(DeleteView):
	model = Organization
	sucess_url = "&empresas"
	template_name = "processes/forms/organization_confirm_delete.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['org_users'] = User.objects.filter(organization__id =self.kwargs['pk'])
		return context	

class OrganizationUpdate(UpdateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "processes/forms/organization_form.html"
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		form = super(OrganizationUpdate, self).get_form(form_class)
		form.fields['name'].label = "Nome da Empresa"
		form.fields['location'].label = "Localização"
		return form

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Bem vindo, {username}")
				return redirect("home")
			else:
				messages.error(request, "Utilizador ou password inválida")

		else:
			messages.error(request, "Utilizador ou password inválida")

	form = AuthenticationForm()
	return render(request,
				  "processes/login.html",
				  {"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("home")


@login_required(login_url='/login')
def utilizadores(request):
	return render(request=request,
					template_name="processes/utilizadores.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "orgs" : Organization.objects.all(), })

@login_required(login_url='/login')
def empresas(request):
	return render(request=request,
					template_name="processes/empresas.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
"orgs" : Organization.objects.all(), })