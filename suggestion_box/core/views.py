from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import LogInForm, SignUpForm, SuggestionForm, VoteForm
from django.contrib.auth import login, authenticate, logout
from .models import Suggestion, Vote
import datetime


# Create your views here.
@login_required
def index(request):
    suggestions = Suggestion.objects.all()
    votes = Vote.objects.all()
    form = VoteForm()
    return render(request, 'core/index.html', context={'suggestions':suggestions, 'votes':votes, 'form':form})

def vote(request, pk):
    suggestions = Suggestion.objects.all()
    form = VoteForm()
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            vote = Vote(
                suggestion = get_object_or_404(Suggestion, pk=pk),
                author = request.user,
                type_vote = cd['type_vote']
            )
            vote.save()
            return render(request, 'core/index.html')
    return render(request, 'core/index.html', context={'suggestions':suggestions, 'form':form})
    

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
        