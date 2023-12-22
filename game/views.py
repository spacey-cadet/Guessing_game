from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    context = {}
    if request.method == 'POST':
        secret_number = request.session.get('secret_number')
        guess = int(request.POST.get('guess'))
        if guess == secret_number:
            context['result'] = "Congratulations! You guessed it right."
            del request.session['secret_number']
        else:
            context['result'] = "Try again! Wrong guess."

    return render(request, 'home.html', context)

def start_game(request):
    request.session['secret_number'] = random.randint(1, 10)
    return HttpResponse('Game started!')