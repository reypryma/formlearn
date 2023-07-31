from django.urls import path

from manga import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
    path('mangas', views.mangas, name='manga'),
]