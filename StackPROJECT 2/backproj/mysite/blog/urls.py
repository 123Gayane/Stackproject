from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('add_question/', add_question, name='add_question'),
    path('get_question/<int:question_id>/', get_question, name='get_question'),
    path('get_all_questions/', get_all_questions, name='get_all_questions'),
    path('add_answer/', add_answer, name='add_answer'),
    path('like_question/', like_question, name='like_question'),
    path('like_answer/', like_answer, name='like_answer'),
    path('log_out/', log_out, name='log_out'),
    path('all_category/', get_all_category, name='all_category'),
    path("user/", get_user),

]