from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('games/', views.index, name='index'),
    path('new_game/', views.new_game, name='new_game'),
    path('new_player/<int:game_id>', views.new_player, name='new_player'),
    path('delete_player/<int:player_id>/', views.delete_player, name='delete_player'),
    path('<int:game_id>/', views.detail, name='detail'),

    # API
    path('api/game', views.UpcomingGameListCreate.as_view()),
    path('api/past_games', views.PastGameListCreate.as_view()),
]
