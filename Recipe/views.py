from django.http import JsonResponse
from .models import Recipes
from .serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipes.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse({'recipes':serializer.data})

    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def recipe_detail(request, id):
    try:
        recipe = Recipes.objects.get(pk=id)
    except Recipes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seriailizer = RecipeSerializer(recipe)
        return Response(seriailizer.data)
    
    elif request.method == 'PUT':
        seriailizer = RecipeSerializer(recipe, data=request.data)
        if seriailizer.is_valid():
            seriailizer.save()
            return Response(seriailizer.data)
        return Response(seriailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)