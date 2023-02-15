from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipes.models import Recipe, Comments, Category
from .forms import RecipeForm, CommentsForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    first_recipe = None
    second_recipe = None
    third_recipe = None
    if first_recipe and second_recipe and third_recipe:
        first_recipe = Recipe.objects.order_by('-id')[0]
        second_recipe = Recipe.objects.order_by('-id')[1]
        third_recipe = Recipe.objects.order_by('-id')[2]

    context = {
               'first_recipe': first_recipe,
               'second_recipe': second_recipe,
               'third_recipe': third_recipe,
                   }
    return render(request, 'recipes/index.html', context)


def check_recipe_owner(request, recipe):
    if recipe.user != request.user:
        raise Http404


def show_recipes(request):
    categories = Category.objects.all()
    cat_id = request.GET.get('categories')
    
    try:
        if cat_id and cat_id.isnumeric():
            category = Category.objects.get(pk=cat_id)
            filtered_recipes = Recipe.objects.filter(category=category).order_by('-publication_date')
        else:
            filtered_recipes = Recipe.objects.all().order_by('-publication_date')
    except Category.DoesNotExist:
        raise Http404("Wybrana kategoria nie istnieje.")

    context = {'filtered_recipes': filtered_recipes,
               'categories': categories}
    return render(request, 'recipes/show_recipes.html', context)


@login_required
def show_my_recipes(request):
    my_recipes = Recipe.objects.filter(user=request.user).order_by('-publication_date')
    paginator = Paginator(my_recipes, 6)
    page_number = request.GET.get('page')

    try:
        my_recipes = paginator.page(page_number)
    except PageNotAnInteger:
        my_recipes = paginator.page(1)
    except EmptyPage:
        my_recipes = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    context = {'my_recipes': my_recipes, 'categories': categories}
    return render(request, 'recipes/show_my_recipes.html', context)


def show_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)


def add_recipe(request):

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()

            return redirect('recipes:show_recipes')
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'recipes/add_recipe.html', context)


def update_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    check_recipe_owner(request, recipe)

    if recipe.user == request.user:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                updated_recipe = form.save(commit=False)
                updated_recipe.user = request.user
                updated_recipe.save()
                return redirect('recipes:show_recipe', pk=pk)
        else:
            form = RecipeForm(instance=recipe)

    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/update_recipe.html', context)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipes:show_recipes')


def search_recipe(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            recipes = Recipe.objects.filter(title__icontains=query)

            context = {'recipes': recipes}
            return render(request, 'recipes/search_recipe.html', context)
        else:
            print("Brak elementów spełniających kryteria wyszukiwania...")
            return render(request, 'recipes/search_recipe.html', {})


def add_comment(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = CommentsForm(instance=recipe)
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=recipe)
        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            comment = Comments(content=content,
                               recipe=recipe,
                               publication_date=datetime.now(),
                               edition_date=datetime.now(),
                               user=user)
            comment.save()
            return redirect('recipes:show_my_recipes')
        else:
            print('Formularz jest nieprawidłowy.')
    else:
        form = CommentsForm()

    context = {'form': form}
    return render(request, 'recipes/add_comment.html', context)


class CommentsDelete(LoginRequiredMixin, DeleteView):
    model = Comments
    context_object_name = 'comment'
    success_url = reverse_lazy('recipes:show_recipes')

