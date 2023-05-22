from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from users.models import Team, Member, Membership
from projects.models import Project, Task, TasksGroup, ProjectMembership
from .forms import NewProjectForm


@login_required(login_url='/login')
def homeView(request):
    return render(request, 'main/home.html')


@login_required(login_url='/login')
def newTeamView(request):
    if request.method == 'POST':
        team_name = request.POST.get('name')
        new_team = Team.objects.create_team(team_name, Member.objects.get(user=request.user))
        new_team.save()
        redirect('/')

    context = {
        'username': request.user.username
    }

    return render(request, 'main/newTeam.html', context)


@login_required(login_url='/login')
def listTeamView(request):
    context = {
        'username': request.user.username,
        'teams': Membership.objects.filter(member=Member.objects.get(user=request.user)),
        'projects': ProjectMembership.objects.filter(member=Member.objects.get(user=request.user))
    }
    return render(request, 'main/list_of_team.html', context)


class NewProjectView(View):

    form = NewProjectForm
    template_name = 'main/newProject.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data['team_name']
            project_name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project = Project.objects.create(name=project_name, description=description)
            project.member.add(Member.objects.get(user=request.user))
            project.save()

            return HttpResponseRedirect('listteam')
        return render(request, self.template_name, {'form': form})


class TeamView(View):

    template_name = 'main/team.html'

    def get(self, request, teamName):
        context = {
            'user': request.user.username,
            'members': Membership.objects.filter(team=Team.objects.get(name=teamName)),
            'ph': 'Email'
        }
        return render(request, self.template_name, context)

    def post(self, request, teamName):
        email = request.POST.get('email')
        member = Member.objects.filter(user=User.objects.filter(email=email).first()).first()
        if member:
            team = Team.objects.get(name=teamName)
            team.members.add(member)
            return HttpResponseRedirect(f'/pr/team/{teamName}')
        else:
            context = {
                'user': request.user.username,
                'members': Membership.objects.filter(team=Team.objects.get(name=teamName)),
                'ph': 'Error-email'
            }
            return render(request, self.template_name, context)


class ProjectView(View):

    template_name = 'main/project.html'

    def get(self, request, projectName):
        project = Project.objects.filter(name=projectName).first()
        member = Member.objects.filter(user=request.user).first()
        if ProjectMembership.objects.filter(project=project, member=member):
            context = {
                'username': member.user.username,
                'taskGroups': project.tasks_groups,
                'ph': 'task-title'
            }
            return render(request, self.template_name, context)
        else:
            return HttpResponse("You dont in this project")

    def post(self, request, projectName):

        project = Project.objects.filter(name=projectName).first()
        member = Member.objects.filter(user=request.user).first()
        if ProjectMembership.objects.filter(project=project, member=member):
            context = {
                'username': member.user.username,
                'taskGroups': project.tasks_groups,
                'ph': 'task-title'
            }
            return render(request, self.template_name, context)
        else:
            return HttpResponse("You dont in this project")
