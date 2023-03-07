from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, PlayerBadge
from .forms import GamePerformanceForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def players_index(request):
  players = Player.objects.all()
  return render(request, 'players/index.html', {
    'players': players
  })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  id_list = player.playerbadges.all().values_list('id')
  playerbadges_player_doesnt_have = PlayerBadge.objects.exclude(id_in=id_list)
  game_performance_form = GamePerformanceForm()
  return render(request, 'players/detail.html', {
    'player': player,
    'game_performance_form': game_performance_form,
    'playerbadges': playerbadges_player_doesnt_have,
  })

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'
  success_url = '/players'

class PlayerUpdate(UpdateView):
  model = Player
  fields = ['paid', 'primary_position', 'secondary_position']
  success_url = '/players'

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players'

def add_game_performance(request, player_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = GamePerformanceForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # player_id FK.
    new_game_performance = form.save(commit=False)
    new_game_performance.player_id = player_id
    new_game_performance.save()
  return redirect('players_detail', player_id=player_id)


