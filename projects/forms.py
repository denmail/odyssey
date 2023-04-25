from django import forms


class NewProjectForm(forms.Form):
    name = forms.CharField(max_length=200)
    team_name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000)
