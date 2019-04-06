from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post, Process, Activity, Role, Organization
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, PostForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView




def snippets(request):
	return render(request=request,
				  template_name="main/snippets.html",
				  context={"posts": Post.objects.all().order_by('-published')})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid(): 
			user = form.save()
			profile= Group.objects.get(name=form.cleaned_data.get('profile'))
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
	fields = ['username']
	sucess_url = "/utilizadores"
	template_name = "main/forms/user_update_form.html"


def deleteUser(request, id):
    user_to_delete = get_object_or_404(User, pk=id).delete()
    return redirect(utilizadores)

def gparea(request):
	return render(request=request,
				  template_name="main/gparea.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})

def processos(request):
	return render(request=request,
				  template_name="main/processos.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all()})

def utilizadores(request):
	return render(request=request,
					template_name="main/utilizadores.html",
					context={"users" : User.objects.all(),})


@login_required(login_url='/login2')
def home(request):
	return render(request=request,
				  template_name="main/homepage.html",
				   context={"procs": Process.objects.all(), "acts": Activity.objects.all(),
				   			"roles": Role.objects.all()	, "users" : User.objects.all(),	
							 "orgs" : Organization.objects.all(),								

				   }
				   )
	

def post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.username = request.user
			messages.success(request, f"Snippet Posted!")
			post.save()
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	form = PostForm()
	return render(request,
				  "main/post.html",
				  context={"form":form})

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




