from django.db import models

# Create your models here.

class Routes(models.Model):
    node_a = models.IntegerField()
    node_b = models.IntegerField()