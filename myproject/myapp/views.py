# In myapp/views.py

from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Welcome to My Django App',
        'message': 'This is a sample Django app!',
        'placeholder1': 'Placeholder 1',
        'placeholder2': 'Placeholder 2',
        'placeholder3': 'Placeholder 3',
        'placeholder4': 'Placeholder 4',
        'placeholder5': 'Placeholder 5',
    }
    return render(request, 'myapp/index.html', context)
