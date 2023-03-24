from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LogInForm(forms.Form):
    username = forms.CharField(max_length=63, label='USERNAME')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='PASSWORD')
    

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        
class SuggestionForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)