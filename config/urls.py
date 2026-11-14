from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import path


def home(_request):
    return redirect("admin:index")


def health(_request):
    return JsonResponse({"status": "ok", "service": "lab6-usuarios"})


urlpatterns = [
    path("", home, name="home"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
]
