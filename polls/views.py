from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Poll, PollVote
from .forms import PollVoteForm

def is_moderator(user):
    return user.is_staff or user.is_superuser

@login_required
def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    try:
        vote = PollVote.objects.get(poll=poll, user=request.user)
        initial = {'option': vote.option.pk}
    except PollVote.DoesNotExist:
        vote = None
        initial = None

    if request.method == 'POST':
        form = PollVoteForm(poll, request.POST)
        if form.is_valid():
            option_pk = form.cleaned_data['option']
            if vote:
                vote.option_id = option_pk
                vote.save()
            else:
                PollVote.objects.create(poll=poll, user=request.user, option_id=option_pk)
            return redirect('poll_results', poll_id=poll.pk)
    else:
        form = PollVoteForm(poll, initial=initial)

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'form': form})

@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    options = poll.options.all()

    results = []
    total_votes = PollVote.objects.filter(poll=poll).count()
    for option in options:
        count = PollVote.objects.filter(poll=poll, option=option).count()
        percent = (count / total_votes * 100) if total_votes > 0 else 0
        results.append({'option': option.text, 'count': count, 'percent': percent})

    return render(request, 'polls/poll_results.html', {
        'poll': poll,
        'results': results,
        'total_votes': total_votes,
    })

@login_required
@user_passes_test(is_moderator)
def poll_create(request):
    from django.forms import modelform_factory
    PollForm = modelform_factory(Poll, fields=['title', 'description'])
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            return redirect('poll_edit', poll_id=poll.pk)
    else:
        form = PollForm()
    return render(request, 'polls/poll_form.html', {'form': form, 'create': True})

@login_required
@user_passes_test(is_moderator)
def poll_edit(request, poll_id):
    from django.forms import modelform_factory
    poll = get_object_or_404(Poll, pk=poll_id)
    PollForm = modelform_factory(Poll, fields=['title', 'description'])
    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            form.save()
            return redirect('poll_list')
    else:
        form = PollForm(instance=poll)
    return render(request, 'polls/poll_form.html', {'form': form, 'create': False})

@login_required
@user_passes_test(is_moderator)
def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')
    return render(request, 'polls/poll_confirm_delete.html', {'poll': poll})
