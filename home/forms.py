from django import forms
from .models import Todo

class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'image', 'starred', 'Degree_of_Importance', 'started', 'board']


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'image', 'starred', 'Degree_of_Importance', 'started', 'board']

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()