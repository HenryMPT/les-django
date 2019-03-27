from django.contrib import admin
from .models import  Post, Organization, Process, Activity, Role, Product
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["username", "published"]}),
		("Body", {"fields":["body"]})
	]
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(Post, PostAdmin)
admin.site.register(Organization)
admin.site.register(Process)
admin.site.register(Activity)
admin.site.register(Role)
admin.site.register(Product)

