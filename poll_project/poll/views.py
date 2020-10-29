from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
# Create your views here.
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    form = CreatePollForm()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = CreatePollForm()
        
    context={'form': form}
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        select_option = request.POST['poll']
        if select_option == 'option1':
            poll.qs_one_cnt += 1
        elif select_option == 'option2':
            poll.qs_two_cnt += 1
        elif select_option=='option3':
            poll.qs_three_cnt += 1
        else:
            return HttpResponse(400,'Invalid form')
        poll.save()
        return redirect('results',poll.id)
    context = {'poll': poll}
    return render(request, 'poll/vote.html', context)

def results(request, poll_id):
    poll =Poll.objects.get(pk=poll_id)
    context={'poll':poll}
    return render(request, 'poll/results.html', context)

def allresults(request):
    allpolls = Poll.objects.all()
    context = {'allpolls': allpolls}
    return render(request, 'poll/allresults.html', context)