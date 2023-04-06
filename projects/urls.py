from django.urls import path


from projects.views import homeView, newTeamView

app_name = 'projects'

urlpatterns = [
    path('', homeView),
    path('newTeam', newTeamView, name='newTeam')
]