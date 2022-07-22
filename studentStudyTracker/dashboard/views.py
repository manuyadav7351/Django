from email import message
from django.shortcuts import redirect, render
from django.contrib import messages
from matplotlib.style import context
from . forms import *

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} Successfully!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request, 'dashboard/notes.html',context)

def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST('is_finished')
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
    

    form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homeworks':homework,'homeworks_done':homework_done,'form':form}
    return render(request, 'dashboard/homework.html',context)

