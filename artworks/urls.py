from django.urls import path
from . import views

app_name = 'artworks'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/search/', views.search_artworks, name='search'),
    path('artwork/<int:artwork_id>/', views.artwork_detail, name='detail'),
]