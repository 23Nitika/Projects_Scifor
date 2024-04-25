from django.shortcuts import render, redirect
from .models import Poll

def index(request):
    latest_polls = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_polls': latest_polls}
    return render(request, 'index.html', context)

def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'results.html', {'poll': poll})

def vote(request, poll_id):
    from django.shortcuts import render, redirect
from .models import Poll, Choice

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = Choice.objects.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('results', poll_id=poll_id)
        else:
            # Handle case where no choice is selected
            pass
    return render(request, 'vote.html', {'poll': poll})


def vote_counts(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    choices = poll.choice_set.all()
    context = {'poll': poll, 'choices': choices}
    return render(request, 'vote_counts.html', context)