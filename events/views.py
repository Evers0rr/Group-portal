from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Event
from .forms import EventForm

def is_moderator(user):
    return user.is_staff or user.is_superuser

def home(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
@user_passes_test(is_moderator)
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
@user_passes_test(is_moderator)
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
@user_passes_test(is_moderator)
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def event_calendar(request):
    events = Event.objects.all()
    return render(request, 'events/event_calendar.html', {'events': events})
