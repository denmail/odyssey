# Generated by Django 4.1.7 on 2023-04-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='projects.task'),
        ),
        migrations.CreateModel(
            name='TasksGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('tasks', models.ManyToManyField(default=None, to='projects.task')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tasks_groups',
            field=models.ManyToManyField(to='projects.tasksgroup'),
        ),
    ]
