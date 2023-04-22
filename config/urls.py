from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vocabulary.views import VocabularyView

router = routers.DefaultRouter()
router.register(r"vocabulary", VocabularyView, basename="vocabulary")

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"api/", include(router.urls))
]
