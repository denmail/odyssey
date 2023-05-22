from django.contrib import admin

# Register your models here.
import projects.models

admin.site.register(projects.models.Project)
admin.site.register(projects.models.Task)
admin.site.register(projects.models.ProjectMembership)
admin.site.register(projects.models.TasksGroup)

