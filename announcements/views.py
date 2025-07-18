from django.shortcuts import render, redirect, get_object_or_404
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, 'announcements/home.html', {'announcements': announcements})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def create_announcement(request):
    form = AnnouncementForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        announcement = form.save(commit=False)
        announcement.author = request.user
        announcement.save()
        return redirect('home')
    return render(request, 'announcements/form.html', {'form': form, 'title': 'Створити оголошення'})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    form = AnnouncementForm(request.POST or None, instance=announcement)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'announcements/form.html', {'form': form, 'title': 'Редагувати оголошення'})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('home')
    return render(request, 'announcements/delete_confirm.html', {'announcement': announcement})
