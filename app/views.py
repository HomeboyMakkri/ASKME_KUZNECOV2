import copy

from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404

QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for questions #{i}',
        'tags': [f'tag{j}' for j in range(3)]
    } for i in range(30)
]


def index(request):
    page = paginate(QUESTIONS, request)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()

    page = paginate(hot_questions, request)

    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(
        request, 'one_question.html',
        {'item': one_question})


def login(request):
    return render(request, 'logIn.html')


def signup(request):
    return render(request, 'registration.html')


def ask(request):
    return render(request, 'ask.html')


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def questions_by_tag(request, tag):
    filtered_questions = [q for q in QUESTIONS if tag in q['tags']]

    if not filtered_questions:
        raise Http404("No questions found for this tag.")

    page = paginate(filtered_questions, request)

    return render(request, 'search_by_tag.html', {'questions': page.object_list, 'page_obj': page, 'tag': tag})
