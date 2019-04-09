from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import User, Process, Activity, Role, Organization, Product
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView, CreateView


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
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	form = NewUserForm()
	return render(request,
				  "main/register.html",
				  {"form":form})

class UserDelete(DeleteView):
	model = User
	sucess_url = "/utilizadores"
	template_name = "main/forms/user_confirm_delete.html"


class UserUpdate(UpdateView):
	model = User
	fields = ['username', 'email', 'organization', 'groups']
	sucess_url = "/utilizadores"
	template_name = "main/forms/user_update_form.html"



def gparea(request):
	return render(request=request,
				  template_name="main/gparea.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})

@login_required(login_url='/login2')
def processos(request):
	return render(request=request,
				  template_name="main/processos.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})


class ProcessCreate(CreateView):
	model = Process
	fields = ['process_name', 'description', 'user' ]
	template_name = "main/forms/process_form.html"

class ProcessUpdate(UpdateView):
	model = Process
	fields = ['process_name', 'description', 'user' ]
	template_name = "main/forms/process_update_form.html"

class ProcessDelete(DeleteView):
	model = Process
	sucess_url = "/processos"
	template_name = "main/forms/process_confirm_delete.html"

@login_required(login_url='/login2')
def utilizadores(request):
	return render(request=request,
					template_name="main/utilizadores.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "orgs" : Organization.objects.all(), })

@login_required(login_url='/login2')
def empresas(request):
	return render(request=request,
					template_name="main/empresas.html",
					context={"users" : User.objects.all(),
					"groups" : Group.objects.all(),
					 "orgs" : Organization.objects.all(), })

class OrganizationCreate(CreateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "main/forms/organization_form.html"


class OrganizationDelete(DeleteView):
	model = Organization
	sucess_url = "&empresas"
	template_name = "main/forms/organization_confirm_delete.html"

class OrganizationUpdate(UpdateView):
	model = Organization
	fields = ['name', 'location']
	template_name = "main/forms/organization_form.html"


@login_required(login_url='/login2')
def home(request):
	return render(request=request,
				  template_name="main/homepage.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all(),
				   			"roles": Role.objects.all()	, "users" : User.objects.all(),	
							 "orgs" : Organization.objects.all(), "prods" : Product.objects.all(),							

				   }
				   )
	

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})


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
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login2.html",
				  {"form":form})




