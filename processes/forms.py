from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from tinymce.widgets import TinyMCE
from django.db import models
from processes.models import Process, Activity, Role, Product
from Users.models import   User, Organization
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    c = (("Funcionario", "FUNCIONARIO"), ("Analista", "ANALISTA")
	 , ("Gestor de Processos", "GESTOR DE PROCESSOS") ,
	 ("Admin", "ADMINISTRADOR"))
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    class Meta:
        model = User
        fields = ("username", "email", "group", "organization", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        profile= Group.objects.get(name=self.cleaned_data.get('group'))
        group = profile
        organization = self.cleaned_data['organization']
        if commit:
            user.save()
            user.groups.add(profile)
        return user

class SwapActivityForm(ModelForm):
    activity_name = forms.CharField(required=True,max_length=200)
    process = forms.ModelMultipleChoiceField(queryset=Process.objects.all())
    description = forms.Textarea()
    role = forms.ModelMultipleChoiceField(queryset=Role.objects.all())

    class Meta:
        model = Activity
        fields = ("activity_name", "process", "description", "role",)

    def save(self, commit=True):
        activity = super(SwapActivityForm, self).save(commit=False)
        activity_name = self.cleaned_data['activity_name']
        grole= Role.objects.get(role_name=self.cleaned_data.get('role'))
     #   process = Process.objects.get(name=self.cleaned_data.get('process'))
        description = self.cleaned_data['description']
        if commit:
            activity.save()
            activity.role.add(grole)
        return activity        