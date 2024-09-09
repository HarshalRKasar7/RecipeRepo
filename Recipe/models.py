from django.db import models

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)
    cooking_time = models.IntegerField(help_text="Minutes")

    def __str__(self) -> str:
        return self.name