from django.shortcuts import render
from django.http import HttpResponse

QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for questions #{i}'
        } for i in range(1, 30)
]

def index(request):
    return render(
        request, 'main.html',
        context={'questions': QUESTIONS}
    )
