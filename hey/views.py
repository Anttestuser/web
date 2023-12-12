from django.http import HttpResponse
from django.shortcuts import render, redirect

from hey.forms import ImageForm
from hey.models import UploadFiles


def show_index(request):
    return render(request, 'index.html')


def show_input(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()

    return render(request, 'input.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def show_output(request):
    return render(request, 'output.html')


def show_output(request):
    if request.method == 'GET':
        images = UploadFiles.objects.all()
        return render(request, 'output.html',
                      {'images': images})
