from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PollPost, PollAnswer, Answer, PollQuestion
from Authenticationsystem.models import Profile
from .forms import CreatePollForm, QuestionCreateForm,AnswerForQuestionForm
