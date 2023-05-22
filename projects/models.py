from django.db import models

from users.models import Member, Team


class Task(models.Model):
    title = models.CharField(max_length=200, default='title')
    created_at = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(default=None)

    def __str__(self):
        return self.title


class TasksGroup(models.Model):
    title = models.CharField(max_length=200, default='title')
    tasks = models.ManyToManyField(Task, default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Task, default=None, null=True, blank=True)
    tasks_groups = models.ManyToManyField(TasksGroup, )
    member = models.ManyToManyField(Member, through="ProjectMembership", default=None)
    owner_team = models.ManyToManyField(Team, default=None)

    def __str__(self):
        return self.name


class ProjectMembership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ROLE = [
        ('1', 'owner'), ('2', 'admin'), ('3', 'workers')
    ]
    role = models.CharField(max_length=8, choices=ROLE)

    def __str__(self):
        return self.role + " " + self.member.user.username + " " + self.project.name
