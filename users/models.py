from django.contrib.auth.models import User
from django.db import models
from projects.models import Project


class Member(models.Model):
    pass


class TeamManager(models.Manager):
    def create_team(self, team_name, owner):
        team = self.create(name=team_name)
        team.owner.add(owner)
        return team


class Team(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ManyToManyField(User, default=None)
    members = models.ManyToManyField(Member, default=None)
    projects = models.ManyToManyField(Project, default=None)
    objects = TeamManager()

