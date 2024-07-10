from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from belbin import settings


class Command(BaseCommand):
    class ErrorMessages:
        ENVIRONMENT = 'No se puede ejecutar este comando en entornos de producción'

    def handle(self, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR(Command.ErrorMessages.ENVIRONMENT))
            return

        User.objects.create_user(
            username='admin',
            password='123',
            is_superuser=True,
            is_staff=True
        )
