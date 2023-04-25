from django.contrib.auth.models import User
from django.db import models
from projects.models import Project


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class TeamManager(models.Manager):
    def create_team(self, team_name, owner):
        team = self.create(name=team_name)
        team.members.add(owner)
        team.projects.through.objects.all().delete()
        return team


class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Member, through="Membership", default=None)
    projects = models.ManyToManyField(Project, default=None)
    objects = TeamManager()

    def __str__(self):
        return self.name


class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ROLE = [
        ('1', 'owner'), ('2', 'admin'), ('3', 'workers')
    ]
    role = models.CharField(max_length=8, choices=ROLE)

    def __str__(self):
        return self.role + " " + self.member.user.username + " " + self.team.name
