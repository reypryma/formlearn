from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'manga/home.html')


def order(request):
    return render(request, 'manga/order.html')


def manga(request):
    return render(request, 'manga/manga.html')