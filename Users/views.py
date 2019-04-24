from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse
from processes.models import Process, Activity, Role, Product
from .models import User, Organization
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid(): 
			user = form.save()
			profile= Group.objects.get(name=form.cleaned_data.get('group'))
			user.groups.add(profile)
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
	#		login(request, user)
	#		messages.info(request, f"You are now logged in as {username}")
			return redirect("processes:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	form = NewUserForm()
	return render(request,
				  "processes/register.html",
				  {"form":form})

class UserDelete(DeleteView):
	model = User
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_confirm_delete.html"


class UserCreate(CreateView):
	model = User
	form_class = NewUserForm
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_form.html"

class UserUpdate(UpdateView):
	model = User
	fields = ['username', 'email', 'organization', 'groups']
	sucess_url = "/utilizadores"
	template_name = "processes/forms/user_update_form.html"


class OrganizationCreate(CreateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "processes/forms/organization_form.html"


class OrganizationDelete(DeleteView):
	model = Organization
	sucess_url = "&empresas"
	template_name = "processes/forms/organization_confirm_delete.html"

class OrganizationUpdate(UpdateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "processes/forms/organization_form.html"


def login2_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("processes:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "processes/login2.html",
				  {"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("processes:homepage")


@login_required(login_url='/login2')
def utilizadores(request):
	return render(request=request,
					template_name="processes/utilizadores.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "orgs" : Organization.objects.all(), })

@login_required(login_url='/login2')
def empresas(request):
	return render(request=request,
					template_name="processes/empresas.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
"orgs" : Organization.objects.all(), })