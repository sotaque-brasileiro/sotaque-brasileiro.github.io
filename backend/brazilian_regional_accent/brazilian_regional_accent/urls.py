"""brazilian_regional_accent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .accent_collector import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"states", views.StateViewSet)
router.register(r"cities", views.CityViewSet)
router.register(r"genders", views.GenderViewSet)
router.register(r"sentences", views.SentenceViewSet)
router.register(r"speakers", views.SpeakerViewSet)
router.register(r"records", views.RecordViewSet)
router.register(r"create_record", views.NewRecordViewSet, basename="create_record")


urlpatterns = [
    path("", include(router.urls)),
    # path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
