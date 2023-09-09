from django import forms

from manga.models import Manga, Volume, SubGenre


class MangaForm(forms.ModelForm):
    volume = forms.ModelChoiceField(
        queryset=Volume.objects.all().order_by('title'),
        widget=forms.Select,  # Use Select widget for a single choice
        required=False  # Make it optional if needed
    )

    class Meta:
        model = Manga
        fields = ['genre', 'sub_genres', 'volume']
        labels = {'genre': 'Genre', 'sub_genres': 'Sub Genre', 'volume': 'Volume'}


class MultipleMangaForm(forms.Form):
    numbers = forms.IntegerField(min_value=2, max_value=5)


class VolumeForm(forms.ModelForm):
    manga = forms.ModelChoiceField(queryset=Manga.objects.all(), label='Associated Manga')

    class Meta:
        model = Volume
        fields = ['title', 'manga']
