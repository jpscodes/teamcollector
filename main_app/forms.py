from django.forms import ModelForm
from .models import GamePerformance, PlayerBadge, Player

class GamePerformanceForm(ModelForm):
  class Meta: 
    model = GamePerformance
    fields = ['date', 'at_bats', 'hits', 'review']

class PlayerBadgeForm(ModelForm):
  class Meta: 
    model = PlayerBadge
    fields = ['name', 'color']

class PlayerForm(ModelForm):
  class Meta: 
    model = Player
    fields = ['name', 'age', 'paid', 'primary_position', 'secondary_position']