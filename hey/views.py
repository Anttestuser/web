from django.shortcuts import render


def show_index(request):
    return render(request, 'index.html')


def show_input(request):
    return render(request, 'input.html')
