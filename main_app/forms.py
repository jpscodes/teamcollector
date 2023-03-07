from django.forms import ModelForm
from .models import GamePerformance, PlayerBadge

class GamePerformanceForm(ModelForm):
  class Meta: 
    model = GamePerformance
    fields = ['date', 'at_bats', 'hits', 'review']

class PlayerBadge(ModelForm):
  class Meta: 
    model = PlayerBadge
    fields = ['name', 'color']