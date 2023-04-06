from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.models import Team

@login_required(login_url='login')
def homeView(request):
    return render(request, 'main/home.html')


@login_required(login_url='login')
def newTeamView(request):
    if request.method == 'POST':
        team_name = request.POST.get('name')
        new_team = Team.objects.create_team(team_name, request.user)
        new_team.save()
        redirect('/')

    return render(request, 'main/newTeam.html')