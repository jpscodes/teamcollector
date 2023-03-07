from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, PlayerBadge
from .forms import GamePerformanceForm, PlayerBadgeForm, PlayerForm


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
  # playerbadges_player_doesnt_have = PlayerBadge.objects.exclude(id_in=id_list)
  game_performance_form = GamePerformanceForm()
  player_badge_form = PlayerBadgeForm()
  player_form = PlayerForm()
  return render(request, 'players/detail.html', {
    'player': player,
    'game_performance_form': game_performance_form,
    'player_badge_form': player_badge_form,
    'player_form': player_form,
    # 'playerbadges': playerbadges_player_doesnt_have,
  })

class PlayerCreate(CreateView):
  model = Player
  fields = ['name', 'age', 'primary_position', 'secondary_position']
  success_url = '/players'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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


# class PlayerBadgeList(ListView):
#   model = PlayerBadge

# class PlayerBadgeDetail(DetailView):
#   model = PlayerBadge

class PlayerBadgeCreate(CreateView):
  model = PlayerBadge
  fields = '__all__'

# class PlayerBadgeUpdate(UpdateView):
#   model = PlayerBadge
#   fields = ['name', 'color']

# class PlayerBadgeDelete(DeleteView):
#   model = PlayerBadge
#   success_url = '/PlayerBadges'

# def assoc_playerbadge(request, player_id, playerbadge_id):
#   Player.objects.get(id=player_id).playerbadges.add(playerbadge_id)
#   return redirect('detail', player_id=player_id)

# def un_assoc_playerbadge(request, player_id, playerbadge_id):
#   Player.objects.get(id=player_id).playerbadges.remove(playerbadge_id)
#   return redirect('detail', player_id=player_id)