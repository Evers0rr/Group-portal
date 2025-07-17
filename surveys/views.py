from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Survey, SurveyQuestion, SurveyResponse, SurveyResponseAnswer
from .forms import SurveyAnswerForm

def is_moderator(user):
    return user.is_staff or user.is_superuser

@login_required
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/survey_list.html', {'surveys': surveys})

@login_required
def survey_detail(request, survey_id, step=0):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.order_by('order')
    step = int(step)
    if step >= len(questions):
        # Завершення опитування
        return redirect('survey_complete', survey_id=survey.pk)

    question = questions[step]

    # Перевірка чи користувач вже відповів на це опитування
    response, created = SurveyResponse.objects.get_or_create(survey=survey, user=request.user)

    if request.method == 'POST':
        form = SurveyAnswerForm(request.POST, question=question)
        if form.is_valid():
            answer_pk = form.cleaned_data['answer']
            # Зберегти відповідь
            # Спочатку видалимо відповідь на це питання якщо існує
            SurveyResponseAnswer.objects.filter(response=response, question=question).delete()
            SurveyResponseAnswer.objects.create(
                response=response,
                question=question,
                answer_id=answer_pk
            )
            return redirect('survey_detail', survey_id=survey.pk, step=step+1)
    else:
        # Якщо вже є відповідь, підставимо у форму
        try:
            existing_answer = SurveyResponseAnswer.objects.get(response=response, question=question)
            initial = {'answer': existing_answer.answer.pk}
        except SurveyResponseAnswer.DoesNotExist:
            initial = None
        form = SurveyAnswerForm(question=question, initial=initial)

    context = {
        'survey': survey,
        'question': question,
        'form': form,
        'step': step,
        'total_steps': len(questions),
    }
    return render(request, 'surveys/survey_detail.html', context)

@login_required
def survey_complete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, 'surveys/survey_complete.html', {'survey': survey})

@login_required
@user_passes_test(is_moderator)
def survey_results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.order_by('order')
    # Зібрати відповіді для кожного питання
    data = []
    for question in questions:
        answers = question.answers.all()
        answer_counts = []
        for answer in answers:
            count = SurveyResponseAnswer.objects.filter(question=question, answer=answer).count()
            answer_counts.append((answer.text, count))
        data.append({'question': question.text, 'answer_counts': answer_counts})

    return render(request, 'surveys/survey_results.html', {'survey': survey, 'data': data})
