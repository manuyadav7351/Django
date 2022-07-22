from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
    path('homework', views.homework, name='homework'),
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('todo', views.todo, name='todo'),
    path('todo_homework/<int:pk>', views.update_todo, name='update-todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('books', views.books, name='books'),
]
