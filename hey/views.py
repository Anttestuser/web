from django.shortcuts import render


def show_index(request):
    return render(request, 'index.html')


def show_input(request):
    # if request.method == 'POST':

    return render(request, 'input.html')
