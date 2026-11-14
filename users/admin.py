from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0
    min_num = 1
    verbose_name_plural = "Perfil y foto en Amazon S3"
    fields = ("phone", "role", "photo", "photo_preview")
    readonly_fields = ("photo_preview",)

    @admin.display(description="Vista previa")
    def photo_preview(self, obj):
        if obj and obj.photo:
            return format_html('<img src="{}" alt="Foto de perfil" class="profile-preview">', obj.photo.url)
        return "Sin foto"


class LabUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ("avatar", "username", "full_name", "email", "profile_role", "is_active", "is_staff")
    list_filter = ("is_active", "is_staff", "profile__role")
    search_fields = ("username", "first_name", "last_name", "email", "profile__phone")
    ordering = ("username",)
    list_per_page = 20

    @admin.display(description="Foto")
    def avatar(self, obj):
        try:
            if obj.profile.photo:
                return format_html('<img src="{}" alt="" class="profile-avatar">', obj.profile.photo.url)
        except Profile.DoesNotExist:
            pass
        initials = ((obj.first_name[:1] + obj.last_name[:1]) or obj.username[:1]).upper()
        return format_html('<span class="profile-initials">{}</span>', initials)

    @admin.display(description="Nombre", ordering="first_name")
    def full_name(self, obj):
        return obj.get_full_name() or "—"

    @admin.display(description="Rol", ordering="profile__role")
    def profile_role(self, obj):
        try:
            return obj.profile.get_role_display()
        except Profile.DoesNotExist:
            return "Sin perfil"


admin.site.unregister(User)
admin.site.register(User, LabUserAdmin)

admin.site.site_header = "Administración de usuarios"
admin.site.site_title = "Laboratorio 6"
admin.site.index_title = "Gestión segura de usuarios"
