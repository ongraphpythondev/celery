from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import datetime

from .form import GenerateRandomUserForm
from .tasks import create_random_user_accounts, send_mails , add_result_to_database
from celery.utils import uuid
from app.models import Celery_Result

# returns a list of generated user accounts
class UsersListView(ListView):
    template_name = 'app/user_list.html'
    model = User

    def get(self, request, *args, **kwargs):
        celery_object = Celery_Result.objects.filter(shown = False).first()
        if celery_object is not None:
            celery_object.shown = True
            celery_object.save()
            messages.success(self.request, celery_object.celery.result)
        return super().get(request, *args, **kwargs)

# A page with the form where we can input the number of accounts to generate
class GenerateRandomUserView(FormView):
    template_name = 'app/generate_random_user.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        task_id = uuid()
        create_random_user_accounts.apply_async(args=[total], task_id=task_id, link=add_result_to_database.s(task_id))
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')


class Send_mail(ListView):
    def get(self, request):
        send_mails.delay()
        messages.success(self.request, 'We are sending email to all the users.')
        return render(request, "app/user_list.html")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 18, minute = 45)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+str(datetime.datetime.now()), task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return render(request, "app/user_list.html")