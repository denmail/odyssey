from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, default='title')
    created_at = models.DateTimeField(auto_now_add=True)
    dead_line = models.DateTimeField(default=None)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Task, default=None, null=True, blank=True)

    def __str__(self):
        return self.name



