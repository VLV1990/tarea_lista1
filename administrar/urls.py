from django.urls import path

from .views import v_index , v_eliminar , v_completado

urlpatterns = [
  path('', v_index),
  path('tarea/<int:tarea_id>/eliminar', v_eliminar),
  path('tarea/<int:tarea_id>/completado', v_completado)
]

