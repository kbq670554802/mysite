from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 未使用模板
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)

    # 使用模板
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request,{
    # 		'latest_question_list': latest_question_list,
    # 	})
    # return HttpResponse(template.render(context))

    # 使用模板快捷写法
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # 捕捉404异常的普通写法
    # try:
    # 	question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExit:
    # 	raise Http404('Question does not exist')

    # 快捷写法
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "Your're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("Your're voting on question %s." % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


#########################通用视图####################################
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published question."""
        # return Question.objects.order_by('-pub_date')[:5]
        # 只有当前时间以前发布的问题才显示
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
