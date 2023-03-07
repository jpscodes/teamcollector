from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class PlayerBadge(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('playerbadges_detail', kwargs={'pk': self.id})
  

class Player(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  paid = models.BooleanField(default=False)
  primary_position = models.CharField(max_length=30)
  secondary_position = models.CharField(max_length=50)

  playerbadges = models.ManyToManyField(PlayerBadge)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  
  def __str__(self):
    return f"{self.name}"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'player_id': self.id})
  
class GamePerformance(models.Model):
  date = models.DateField('Game Date')
  at_bats = models.IntegerField()
  hits = models.IntegerField()
  review = models.CharField(max_length=200)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.hits} on {self.date}"
  
  class Meta:
    ordering = ['-date']

