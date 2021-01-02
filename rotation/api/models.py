from django.db import models
import random
import string

# Create your models here.

def code_generator():
    length = 7

    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

class Room(models.Model):
    code            = models.CharField(max_length=10, default=code_generator, unique=True)
    host            = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip   = models.IntegerField(null=False, default=1)
    created         = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

