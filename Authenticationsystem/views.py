from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomCreationForm
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpResponse
from django.urls import resolve
from .forms import ProfileEditeForm
from .models import Profile
import sys
from django.shortcuts import render, get_object_or_404, redirect
from portfolio.models import Project

# from ..portfolio.models import Project


def registration_view(request):
    if request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = Profile.objects.create(
                name=user.username,
                ava="ava/default_ava.jpg",
                user=user,
                description="Zero info",
                first_name = user.first_name,
                last_name = user.last_name
            )
            profile.save()
            return redirect("portfolio" , user.id)
    else:
        form = CustomCreationForm()
    return render(request, template_name="auth/register.html", context={'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("portfolio", request.user.id)
            else:
                print('error')
    else:
        form = AuthenticationForm()
    return render(request, template_name="auth/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("annonce-home")


class Profile_action:
    @staticmethod
    def profile_view(request, user_id):
        profile = get_object_or_404(Profile, id=user_id)
        if profile.isOpen or profile.user == request.user or request.user.is_staff or request.user.is_superuser:
            return render(request, template_name='auth/profile.html', context={
                'profile': profile, })
        else:
            raise PermissionDenied()

    @staticmethod
    def profile_edit(request):
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == "POST":
            form = ProfileEditeForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("portfolio", request.user.id)
            return render(request, "auth/profile_edit.html", context={"form": form, "profile": profile})
        else:
            form = ProfileEditeForm(instance=profile)
        return render(request, "auth/profile_edit.html", context={"form": form, "profile": profile})

    @staticmethod
    def profiles(request):
        profiles = Profile.objects.all()

        return render(request, 'auth/profiles.html', context={'profiles':profiles})