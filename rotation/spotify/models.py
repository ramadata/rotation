from django.db import models

# Create your models here.

class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    token_type = models.CharField(max_length=50)
    access_token = models.CharField( max_length=150)
    refresh_token = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    expires_in = models.DateTimeField()
