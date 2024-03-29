from django.urls import path
from salas.views.classView import atualizar_sala_api, listar_salas_api, excluir_sala_api, detalhes_sala_api, criar_sala_api
from salas.views.reserveView import listar_reservas_sala_api, detalhes_reserva_api, criar_reserva_api, atualizar_reserva_api, excluir_reserva_api

urlpatterns = [
    path('salas/', listar_salas_api),
    path('salas/criar', criar_sala_api),
    path('salas/<str:sala_id>/', detalhes_sala_api),
    path('salas/<str:sala_id>/atualizar/', atualizar_sala_api),
    path('salas/<str:sala_id>/excluir/', excluir_sala_api),
    path('salas/<str:sala_id>/reservas/', listar_reservas_sala_api),
    # path('salas/<str:sala_id>/reservas/<str:reserva_id>/', detalhes_reserva_api),
    path('salas/<str:sala_id>/reservas/criar/', criar_reserva_api),
    path('salas/<str:sala_id>/reservas/<str:reserva_id>/atualizar/', atualizar_reserva_api),
    path('salas/<str:sala_id>/reservas/<str:reserva_id>/excluir/', excluir_reserva_api),
]
