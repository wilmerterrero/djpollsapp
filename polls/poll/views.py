from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict

from .models import Question, Choice


def index(self):
    """
    Get questions and display them
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(self, 'polls/index.html', context)


def detail(self, question_id):
    """
    Show specific question and choices
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(self, 'polls/detail.html', {'question': question})


def results(self, question_id):
    """
    Get question and display results
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(self, 'polls/results.html', {'question': question})


def vote(self, question_id):
    """
    Vote for a question choice
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=self.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(self, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))


def get_all(self):
    """
    Retrieve all questions in JSON
    """
    questions = Question.objects.all()
    return JsonResponse(list(questions.values()), safe=False)


def get(self, question_id):
    """
    Show specific question and choices in JSON
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return JsonResponse(model_to_dict(question), safe=False)
