import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from project_celery import settings
from django.core.mail import send_mail
from celery import shared_task
from django_celery_results.models import TaskResult
from app.models import Celery_Result


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        print("user created")
        User.objects.create_user(username=username, email=email, password=password)
    print(TaskResult.objects.all())
    return '{} random users created with success!'.format (total)

@shared_task
def send_mails():
    users = User.objects.all()
    print("started sending mail")
    for user in users:
        subject = 'welcome to Ongraph family'
        message = f'Hi {user.username}, This is computer generated email'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email ]
        send_mail( subject = subject, message = message,from_email= email_from,recipient_list= recipient_list )
    return 'Email is sended'

@shared_task
def add_result_to_database(request, task_id):
    print(task_id)
    task_result_object = TaskResult.objects.get(task_id = task_id)
    celery_result_object = Celery_Result.objects.create(celery = task_result_object) 
    return 'Added result to the DB'