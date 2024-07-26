
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordModelViewSet

router = DefaultRouter()
router.register(r'records', RecordModelViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),
]

