from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
# Create your views here.
from Authenticationsystem.models import Profile
from .forms import PhotoForm


def view_photo(request, owner_id):
    user = get_object_or_404(Profile , id = owner_id)
    photos = Photo.objects.filter(owner = user)
    return render(request, template_name="arts/your_galery.html",context={'user':user,'photos':photos})


def add_photo(request):
    user = get_object_or_404(Profile, user = request.user )
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('galery', user.id)
    else:
        form = PhotoForm()
    return render(request,template_name='arts/photo_add.html', context={'form':form,'user':user})

def delete_photo(request, photo_id):
    photo = get_object_or_404(Profile, id = photo_id)
    user = get_object_or_404(Profile, user = photo.owner)
    if request.user == photo.owner or request.user.is_staff:
        photo.delete()
        redirect('galery', user.id)
    return render()