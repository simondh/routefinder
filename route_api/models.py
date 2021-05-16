from django.db import models

# Create your models here.

class Routes(models.Model):
    node_a = models.IntegerField()
    node_b = models.IntegerField()

    def __str__(self):
        return (f"{self.node_a} : {self.node_b}")