from django.urls import path

from manga import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('manga', views.manga, name='manga')
]