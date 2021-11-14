from django.http import Http404
from django.shortcuts import render, HttpResponse,get_object_or_404
from polls.models import Question,Choice
from django.template import loader
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:10]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'index.html', context)



def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exit')
    question = get_object_or_404(Question,pk = question_id) # 和上面方式等效
    return render(request, 'detail.html', {'question': question})


# 类视图和index函数视图功能一样
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('pub_date')[:10]

# 类视图和detail函数视图功能一样
class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': 'You didn\'t slect any choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})