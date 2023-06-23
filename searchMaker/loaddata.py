import csv
import os
import django
from dish_search.models import Restaurent
# dish_search.models import Restaurent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dish_search_app.settings')
django.setup()

with open('restaurants_small.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        id = row[0]
        name = row[1]
        location = row[2]
        items = row[3]
        lat_long = row[4]
        full_details = [5]
        dish = Restaurent(id = id, name = name, location = location, items =items, lat_long = lat_long, full_details= full_details)
        dish.save()


