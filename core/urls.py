from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, ParticipanteViewSet

router = DefaultRouter()
router.register('eventos', EventoViewSet)
router.register('participantes', ParticipanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
