from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import HttpResponse
from django.urls import resolve
from .forms import ProjectForm, MedaiAddForm
from .models import Project, Media

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from Authenticationsystem.models import Profile

# Create your views here.
from .models import user_img_path


class Projects:
    @login_required
    def create_project(request):
        if request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                print(form)
                form.instance.owner_id = request.user.id
                form.save()
                return redirect("projects", request.user.id)
            return render(request, "portfolio/project_create.html", context={"form": form})
        else:
            return render(request, "portfolio/project_create.html")

    def edit_project(request, project_id):
        project = get_object_or_404(Project, id=project_id)
        if request.user == project.owner:
            if request.method == "POST":
                form = ProjectForm(request.POST, instance=project)
                if form.is_valid():
                    form.save()
                    return redirect("projects", request.user.id)
            else:
                form = ProjectForm()
            return render(request, "portfolio/project_edit.html", context={"project": project, "form": form})
        else:
            raise PermissionDenied()

    def delete_project(request, project_id):
        project = get_object_or_404(Project, id=project_id)
        if request.user == project.owner:
            project.delete()
            return redirect("projects", request.user.id)
        else:
            raise PermissionDenied()

    def projects(request,user_id):
        user = get_object_or_404(Profile, id=user_id)
        projects = Project.objects.filter(owner=user.user)
        return render(request , template_name="portfolio/your_projects.html",context={"projects":projects,"user":user})

    def project_view(request,project_id):
        project = get_object_or_404(Project, id=project_id)
        medias = Media.objects.filter(owner = project.owner)
        return render(request,template_name="portfolio/your_project.html", context={"project": project,"medias":medias})

    def projectMediaAdd(request, project_id):
        project = get_object_or_404(Project, id=project_id)
        if request.method == "POST":
            form = MedaiAddForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return redirect("project", project_id)
        else:
            form = MedaiAddForm()
        return render(request, "portfolio/add_info.html", context={"project": project,"form":form})
