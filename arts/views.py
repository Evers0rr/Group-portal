from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
# Create your views here.
from Authenticationsystem.models import Profile
from .forms import PhotoForm


def view_photo(request, owner_id):
    user = get_object_or_404(Profile , id = owner_id)
    photos = Photo.objects.filter(owner = user)
    return render(request, template_name="arts/your_galery.html",context={'user':user,'photos':photos})

def view_photos(request):
    if request.user.is_staff:
        photos = Photo.objects.all()
        return render(request, template_name="arts/admin_arts.html",context={'photos':photos})
    else:
        PermissionDenied()
def add_photo(request):
    user = get_object_or_404(Profile, user = request.user )
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = user
            photo.save()
            return redirect('galery', user.id)
    else:
        form = PhotoForm()
    return render(request,template_name='arts/photo_add.html', context={'form':form,'user':user})

def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id = photo_id)
    user = get_object_or_404(Profile, user = photo.owner.user)
    if request.user == photo.owner.user or request.user.is_staff:
        photo.delete()
        return redirect('galery', user.id)
    else:
        raise PermissionDenied()


def admin_photo_accept(request, photo_id):
    photo = get_object_or_404(Photo, id = photo_id)
    if request.user.is_staff:
        photo.is_applied = True
        photo.save()
        return redirect('adminCheakGalery')
    else:
        raise PermissionDenied()

def admin_photo_delete(request, photo_id):
    photo = get_object_or_404(Photo, id = photo_id)
    if request.user.is_staff:
        photo.delete()
        return redirect('adminCheakGalery')
    else:
        raise PermissionDenied()