from django.urls import path
from . import views
from .views import RecipeDelete, CommentsDelete

app_name = 'recipes'


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.show_recipes, name='show_recipes'),
    path('my-recipes/', views.show_my_recipes, name='show_my_recipes'),
    path('recipe/<int:pk>/', views.show_recipe, name='show_recipe'),
    path('recipe/add-recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:pk>/update-recipe/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:pk>/delete-recipe/', RecipeDelete.as_view(), name='recipe-delete'),
    path('recipe/search/', views.search_recipe, name='search_recipe'),
    path('recipe/<int:pk>/add-comment/', views.add_comment, name='add_comment'),
    path('recipe/<int:pk>/delete-comment/', CommentsDelete.as_view(), name='comment-delete'),
]

