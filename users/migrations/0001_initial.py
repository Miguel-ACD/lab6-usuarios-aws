from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("auth", "0012_alter_user_first_name_max_length")]
    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone", models.CharField(blank=True, max_length=20, verbose_name="teléfono")),
                ("role", models.CharField(choices=[("ADMIN", "Administrador"), ("USER", "Usuario")], default="USER", max_length=10, verbose_name="rol")),
                ("photo", models.ImageField(blank=True, upload_to="profiles/%Y/%m/", verbose_name="foto de perfil")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="creado")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="actualizado")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="profile", to=settings.AUTH_USER_MODEL, verbose_name="usuario")),
            ],
            options={"verbose_name": "perfil", "verbose_name_plural": "perfiles", "ordering": ["user__username"]},
        )
    ]
