from django.urls import path


from projects.views import homeView, newTeamView, listTeamView, NewProjectView

app_name = 'projects'

urlpatterns = [
    path('', homeView),
    path('newTeam', newTeamView, name='newTeam'),
    path('listTeam', listTeamView, name='listTeam'),
    path('newProject', NewProjectView.as_view(), name='newProject')
]