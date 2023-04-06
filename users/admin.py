from django.contrib import admin

# Register your models here.
import users.models

admin.site.register(users.models.Team)
admin.site.register(users.models.Member)
