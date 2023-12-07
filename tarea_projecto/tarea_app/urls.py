# tarea_app/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from tarea_app.views import TareaViewSet 
from .views import TareaListCreateView, TareaDetailView, task_list, task_detail
from . import views

router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')


urlpatterns = [
    path('api/tareas/', TareaListCreateView.as_view(), name='tarea-list-create'),
    path('api/tareas/<int:pk>/', TareaDetailView.as_view(), name='tarea-detail'),
    path('tareas/', task_list, name='tarea-list'),
    path('tareas/<int:pk>/', task_detail, name='tarea-detail-template'),
    path('tarea/completada/<int:id_tarea>/', views.marcar_completada, name='marcar-completada'),
]