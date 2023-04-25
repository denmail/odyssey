from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from users.models import Team, Member, Membership
from projects.models import Project
from .forms import NewProjectForm


@login_required(login_url='login')
def homeView(request):
    return render(request, 'main/home.html')


@login_required(login_url='login')
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


@login_required(login_url='login')
def listTeamView(request):
    context = {
        'username': request.user.username,
        'teams': Membership.objects.filter(member=Member.objects.get(user=request.user))
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
            team = Team.objects.get(name=team_name)
            project = Project.objects.create(name=project_name, description=description)
            project.save()
            team.projects.add(project)
            team.save()

            return HttpResponseRedirect('listTeam')
        return render(request, self.template_name, {'form': form})
