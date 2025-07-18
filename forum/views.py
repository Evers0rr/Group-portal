from django.shortcuts import render

def forum_home(request):
    return render(request, 'forum/forum_home.html')
