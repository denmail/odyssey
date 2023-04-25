from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from users.models import Team, Member, Membership


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


@login_required(login_url='login')
class ProjectView(View):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
