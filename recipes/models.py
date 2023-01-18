from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    """Owner of the recipe."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class DifficultyLevel(models.Model):
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level


class Recipe(models.Model):
    """Recipe added by the user."""
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    preparation_time = models.CharField(max_length=100)
    servings = models.CharField(max_length=200)
    ingredients = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    owner = models.CharField(max_length=200)
    level = models.ForeignKey(DifficultyLevel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Comments of recipes written by registration."""
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, related_name='recipes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return f"{self.content} - {self.user}"
