from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import LogInForm, SignUpForm, SuggestionForm
from django.contrib.auth import login, authenticate, logout
from .models import Suggestion
import datetime

# Create your views here.
@login_required
def index(request):
    suggestions = Suggestion.objects.all()
    return render(request, 'core/index.html', {'suggestions':suggestions})

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    return render(request, 'core/sign_up.html', context={'form': form})

def log_in(request):
    form = LogInForm()
    message = ''
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('index')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'core/log_in.html', context={'form': form, 'message': message})

def log_out(request): 
    logout(request)
    return redirect('log_in')

def create_suggestion(request):
    form = SuggestionForm()
    if request.method == 'POST':
        form =SuggestionForm(request.POST)
        # user = request.user
        if form.is_valid():
            cd = form.cleaned_data
            suggestion = Suggestion(
                title = cd['title'],
                description = cd['description'],
                author = request.user,
                date = datetime.datetime.now()
            )
            suggestion.save()
            return redirect('index')
    else:
        form = SuggestionForm()
    return render(request, 'core/new_suggestion.html', context={'form':form})
        