from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('players/', views.players_index, name='players_index'),
  path('players/<int:player_id>/', views.players_detail, name='players_detail'),
  path('players/create/', views.PlayerCreate.as_view(), name='player_create'),
  path('players/<int:pk>/update', views.PlayerUpdate.as_view(), name='player_update'),
  path('players/<int:pk>/delete', views.PlayerDelete.as_view(), name='player_delete'),
  path('players/<int:player_id>/add_game_performance/', views.add_game_performance, name='add_game_performance'),
  path('playerbadge/create/', views.PlayerBadgeCreate.as_view(), name='playerbadge_create'),
]