from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Pattern, Group, Sentence, Tags, Verb
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

admin.site.register(Pattern)
admin.site.register(Group)
admin.site.register(Sentence)
admin.site.register(Tags)
admin.site.register(Verb)