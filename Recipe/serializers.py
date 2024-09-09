from rest_framework import serializers
from .models import Recipes

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'name', 'description', 'ingredients', 'instructions','cooking_time']