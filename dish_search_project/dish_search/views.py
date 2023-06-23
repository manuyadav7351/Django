from django.shortcuts import render
from .models import Restaurant

def search_dish(request):
    dish_name = request.GET.get('dish_name')
    matched_restaurants = []

    if dish_name:
        matched_restaurants = Restaurant.objects.filter(items__contains=dish_name)

    context = {
        'dish_name': dish_name,
        'matched_restaurants': matched_restaurants,
    }

    return render(request, 'dish_search/search.html', context)
