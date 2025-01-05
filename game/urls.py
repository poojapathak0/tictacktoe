from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game_view'),
    path('new/', views.new_game, name='new_game'),
    path('move/<int:game_id>/<int:position>/', views.make_move, name='make_move'),
]
