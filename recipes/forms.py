from django import forms
from .models import Owner, Category, Recipe, Comments, DifficultyLevel


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name',)
        labels = {
            'name': '',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class DifficultyLevelForm(forms.ModelForm):
    class Meta:
        model = DifficultyLevel
        fields = ('level',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['publication_date', 'edition_date', 'user']
        labels = {
            'image': 'Dodaj zdjęcie jedzonka:',
            'title': '',
            'preparation_time': '',
            'servings': '',
            'ingredients': '',
            'content': '',
            'publication_date': '',
            'category': 'Wybierz kategorię:',
            'owner': 'Kto jest właścicielem przepisu?',
            'level': 'Wybierz poziom trudności',

        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Nazwa przepisu'
                                            }),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Czas przygotowania'
                                                       }),
            'servings': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Ilość porcji'
                                               }),
            'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 10,
                                                 'class': 'form-control',
                                                 'placeholder': 'Składniki'
                                                 }),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20,
                                             'class': 'form-control',
                                             'placeholder': 'Treść przepisu'
                                             }),
            'owner': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Np. Ty, Jadłonomia...'
                                            }),
            'category': forms.Select(attrs={'class': 'form-control'
                                            }),
            'level': forms.Select(attrs={'class': 'form-control'
                                         }),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', )
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20,
                                      'class': 'form-control'})
        }
