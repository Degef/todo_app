from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def home(request):
	context = {
		'todos': Todo.objects.all()
	}
	return render(request, 'todo/home.html', context)

def add_todo(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your todo has been added!')
			return redirect('home')
	else:
		form = TodoForm()
	return render(request, 'todo/add_todo.html', {'form': form})

def delete(request, pk):
	Todo.objects.get(id=pk).delete()
	messages.success(request, 'Your todo has been deleted!')
	return redirect('home')

def update(request, pk):
	todo = Todo.objects.get(id=pk)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your todo has been updated!')
			return redirect('home')
	else:
		form = TodoForm(instance=todo)
	return render(request, 'todo/update.html', {'form': form})