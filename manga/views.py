from django.forms import formset_factory
from django.shortcuts import render

from manga.form import MangaForm, MultipleMangaForm
from manga.models import Manga


# Create your views here.
def home(request):
    return render(request, 'manga/home.html')


def order(request):
    multiple_form = MultipleMangaForm()

    if request.method == 'POST':
        filled_form = MangaForm(request.POST, request.FILES)
        bought_manga_pk = None
        if filled_form.is_valid():
            bought_manga = filled_form.save()
            bought_manga_pk = bought_manga.pk
            note = 'Thanks for buying! Your %s %s and %s pizza is on its way!' % \
                   (filled_form.cleaned_data['genre'], filled_form.cleaned_data['sub-genre'],
                    filled_form.cleaned_data['volume']
                    )
            filled_form = MangaForm()
        else:
            note = 'Order was not created, please try again'
        return render(request, 'manga/order.html',
                      {'multiple_form': multiple_form, 'manga_form': filled_form, 'note': note,
                       'bought_manga_pk': bought_manga_pk})
    else:
        form = MangaForm()
        return render(request, 'manga/order.html', {'manga_form': form, 'multiple_form': multiple_form})


def edit_order(request, pk):
    manga = Manga.objects.get(pk=pk)
    form = MangaForm(instance=manga)
    if request.method == 'POST':
        filled_form = MangaForm(request.POST, instance=manga)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your order has been processed.'
            return render(request, 'manga/edit_order.html', {'manga-form': form, 'manga': manga, 'note': note})
    return render(request, 'manga/edit_order.html', {'manga-form': form, 'manga': manga})


def mangas(request):
    number_of_manga = 2
    filled_multiple_pizza_form = MultipleMangaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_manga = filled_multiple_pizza_form.cleaned_data['number']
    manga_form_set = formset_factory(MangaForm, extra=number_of_manga)
    formset = manga_form_set()
    if request.method == 'POST':
        filled_formset = manga_form_set(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['genre'])
            note = 'Manga have been purchased'
        else:
            note = 'Order was not created, please try again'

        return render(request, 'manga/manga.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'manga/manga.html', {'formset': formset})



