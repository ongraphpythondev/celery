from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app.views import GenerateRandomUserView, UsersListView, Send_mail, schedule_mail

urlpatterns = [
    url('users/', UsersListView.as_view(), name='users_list'),
    url('generate/', GenerateRandomUserView.as_view(), name='generate'),
    url('send_mail/', Send_mail.as_view(), name='send_mail'),
    path('schedulemail/', schedule_mail, name="schedulemail"),

]