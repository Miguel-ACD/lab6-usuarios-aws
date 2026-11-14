import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from users.models import Profile


class Command(BaseCommand):
    help = "Crea o actualiza el administrador definido por variables de entorno"

    def handle(self, *args, **options):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if not all((username, email, password)):
            self.stdout.write("Administrador omitido: faltan variables DJANGO_SUPERUSER_*")
            return

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()
        Profile.objects.get_or_create(user=user, defaults={"role": Profile.Role.ADMIN})
        self.stdout.write(self.style.SUCCESS("Administrador creado" if created else "Administrador actualizado"))
