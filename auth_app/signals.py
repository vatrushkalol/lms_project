from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver, Signal
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils  import  timezone

account_access = Signal()


def send_login_user_email(**kwargs):
    template_name = 'registration/account_access_email.html'
    request = kwargs['request']
    context = {
        'request': request,
        'message': f"В ваш аккаунт {request.POST['username']} был выполнен вход {timezone.now().isoformat}"
                   f"\nЕсли Вы не совершали вход то рекомендуется немедленно сменить пароль."


    }
    email = EmailMessage(subject='Вход в аккаунт. Онлайн образование.',
                         body=render_to_string(template_name, context),
                         to=[request.POST['username']]
                         )
    email.content_subtype = 'html'
    email.send(fail_silently=True)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def grant_pupil_rights(sender, instance, created=True, **kwargs):
    if created:
        pupil = Group.objects.filter(name='Ученик')
        instance.groups.set(pupil)
        print(f'Пользователь {instance} успешно добавлен в группу "Ученик"')

account_access.connect(send_login_user_email)