from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  User, Organization, Process, Activity, Role, Product
from tinymce.widgets import TinyMCE
from django.db import models
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm

# Register your models here.




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('organization',)


class MyUserAdmin(UserAdmin):
        add_form = CustomUserCreationForm
        fieldsets = UserAdmin.fieldsets + (
                (None, {'fields': ('organization',)}),
)

class UserAdmin(admin.ModelAdmin):
		form = NewUserForm




admin.site.register(User, MyUserAdmin)
admin.site.register(Organization)
admin.site.register(Process)
admin.site.register(Activity)
admin.site.register(Role)
admin.site.register(Product)

