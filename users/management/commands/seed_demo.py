import base64

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from users.models import Profile


AVATAR_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9ZqNAAAAAASUVORK5CYII="
)


class Command(BaseCommand):
    help = "Crea un usuario de demostración y guarda su avatar en el almacenamiento configurado"

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(
            username="usuario_aws",
            defaults={
                "first_name": "Usuario",
                "last_name": "Demostración",
                "email": "usuario.aws@example.com",
                "is_active": True,
            },
        )
        user.set_unusable_password()
        user.save()

        profile, _ = Profile.objects.get_or_create(user=user)
        profile.phone = "987654321"
        profile.role = Profile.Role.USER
        if not profile.photo:
            profile.photo.save("avatar-demo.png", ContentFile(AVATAR_PNG), save=False)
        profile.save()
        self.stdout.write(self.style.SUCCESS(f"Usuario listo: {user.username} | {profile.photo.name}"))
