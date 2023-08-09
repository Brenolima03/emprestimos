from django.urls import path, include
from rest_framework import routers
from .views import EmprestimoViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register(r'emprestimo', EmprestimoViewSet)
router.register(r'cliente', ClienteViewSet)  # Registre o ClienteViewSet

urlpatterns = [
    path('', include(router.urls)),
]
