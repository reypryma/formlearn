from django.shortcuts import render

from manga.form import MangaForm


# Create your views here.
def home(request):
    return render(request, 'manga/home.html')


def order(request):
    return render(request, 'manga/order.html', {'manga-form': form})


def manga(request):
    return render(request, 'manga/manga.html')