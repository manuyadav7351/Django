from django.urls import path
from dish_search import views

urlpatterns = [
    path('', views.search_dish, name='dish_search'),
]