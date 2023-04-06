from django.contrib import admin

# Register your models here.
import projects.models

admin.site.register(projects.models.Project)