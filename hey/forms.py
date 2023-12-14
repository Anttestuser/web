from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['name', 'file']

from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['name', 'file']
