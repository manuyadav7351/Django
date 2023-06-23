from django import forms

class DishSearchForm(forms.Form):
    dish_name = forms.CharField(label='Dish Name', max_length=100)