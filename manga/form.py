from django import forms

from manga.models import Manga, Volume


class MangaForm(forms.ModelForm):
    volume = forms.ModelChoiceField(queryset=Volume, empty_label=None, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Manga
        fields = ['genre', 'sub_genre', 'volume']
        labels = {'genre': 'Genre', 'sub_genre': 'Sub Genre', 'volume': 'Volume'}
