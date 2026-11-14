from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        USER = "USER", "Usuario"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="usuario")
    phone = models.CharField("teléfono", max_length=20, blank=True)
    role = models.CharField("rol", max_length=10, choices=Role.choices, default=Role.USER)
    photo = models.ImageField("foto de perfil", upload_to="profiles/%Y/%m/", blank=True)
    created_at = models.DateTimeField("creado", auto_now_add=True)
    updated_at = models.DateTimeField("actualizado", auto_now=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        ordering = ["user__username"]

    def __str__(self):
        return f"Perfil de {self.user.get_full_name() or self.user.username}"
