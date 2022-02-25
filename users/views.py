from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from .utils import searchAuthors, paginateAuthors


# Create your views here.
def users(request):
    authors, search_query = searchAuthors(request)

    custom_range, authors = paginateAuthors(request, authors, 6)

    context = {
        'title': 'Authors - NOELIS Author Blog',
        'authors': authors,
        'search_query': search_query,
        'custom_range': custom_range,
    }

    return render(request, 'users/profiles.html', context)


def author(request, pk):
    author = Profile.objects.get(id=pk)

    context = {
        'title': 'Author - NOELIS Author Blog',
        'author': author,
    }

    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('users')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {
        'title': 'Login - NOELIS Author Blog',
    }

    return render(request, 'users/login-register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {
        'title': 'Register - NOELIS Author Blog',
        'page': page,
        'form': form,
    }

    return render(request, 'users/login-register.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    context = {
        'title': 'Account - NOELIS Author Blog',
        'profile': profile,
    }
    
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {
        'title': 'Edit Account - NOELIS Author Blog',
        'form': form,
    }

    return render(request, 'users/profile-form.html', context)
