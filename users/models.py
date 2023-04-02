from django.contrib.auth.models import User
from django.db import models
from projects.models import Project

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Team(models.Model):
    members = models.ManyToManyField(Member)
    projects = models.ManyToManyField(Project)