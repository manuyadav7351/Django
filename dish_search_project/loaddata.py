import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dish_search_project.settings")

import django
django.setup()

from dish_search.models import Restaurant
from dish_search.models import Items

with open('restaurants_small.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Restaurant.objects.create(
            id=row['id'],
            name=row['name'],
            location=row['location'],
            items=row['items'],
            lat_long=row['lat_long'],
            full_details=row['full_details'],
            )
        items = row['items'].split(',')

        for item in items:
            item_name, item_price = item.split(':')
            Items.objects.create(name = item_name, price = item_price, Restaurant=Restaurant)
    

